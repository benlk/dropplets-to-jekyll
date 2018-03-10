#! python
# python2, that is
#
# Ben Keith, March 2018
#
# This script will convert Markdown files formatted for use with the Dropplets
# flat-file CMS to the format for the static site generator Jekyll.
#
# Based on https://gist.github.com/tazjel/8171963

import os, sys, logging, cgi, frontmatter, re

html_escape_table = {
    "'": u"&#39;",
}

def html_escape( text ):
    """
    Produce entitites within text.
    https://wiki.python.org/moin/EscapingHtml
    """
    text = cgi.escape( text, quote=True )
    cheese ="".join(html_escape_table.get(c,c) for c in text)
    return  cheese 

def convert_to_frontmatter( filename ):
    dropplets_file = open( filename, 'r' )
    lines = dropplets_file.readlines()
    dropplets_file.close();

    logging.info( 'opening ' + filename )

    try:
        lines.insert( 6, u'---\n' )
        if u'#' not in lines[0]:
            lines[0] = u'# \'' + lines[0] + '\''

        lines[0] = html_escape( lines[0] )           # all the things
        lines[0] = lines[0].replace( u'# ', '' , 1 ) # remove leading ''
        lines[0] = lines[0].rstrip()                 # remove trailing newlines
        lines[0] = u'title: \'' + lines[0]  + '\'\n' # wrap in quotes

        lines[1] = lines[1].replace( u'- ', u'author: ', 1 )
        lines[2] = lines[2].replace( u'- ', u'twitter_handle: ', 1 ).replace( u'@', u'' )
        lines[3] = lines[3].replace( u'- ', u'date: ', 1 )
        lines[4] = lines[4].replace( u'- ', u'categories: ', 1 )
        lines[5] = lines[5].replace( u'- ', u'classes: ', 1 )

        # After this point, we'll be working from the bottom of the front matter up to the top, maybe inserting new lines after the one we parse.

        # make post status an actual thing
        if u'draft' in lines[5]:
            lines.insert( 6, u'status: draft\n' )
            lines[5] = lines[5].replace( u'draft', u'' )

        # Some things might have a time; split that out
        time = re.compile( r'\d:\d\d' )
        if re.search( time, lines[3] ):
            day_time = lines[3].split( ' ', 2 )
            lines[3] = u'date: ' + day_time[1] + '\n'
            lines.insert(4, u'time: ' + day_time[2] ) # no newline here because it's already there

        lines[5] = lines[5].replace( u'published', u'' )

        lines.insert( 0, u'---\n' )

    except IndexError:
        logging.error( 'IndexError in' + filename )
        logging.info( lines )
        exit()

    output_file = open( filename, 'w' )
    output_file.writelines( lines )
    output_file.close()

    logging.info( '    closing ' + filename )

def frontmatter_parse( filename ):
    try:
        post = frontmatter.load( filename )
        print( post.metadata )
    except:
        logging.warn( filename )


def main():
    if sys.argv < 2:
        error_msg( 'too few arguments, please specify a filename' )
    convert_to_frontmatter( sys.argv[1] )
    frontmatter_parse( sys.argv[1] )

if __name__ == '__main__':
    main();
