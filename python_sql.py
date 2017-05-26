# -*- coding: utf-8 -*-

def parse_statement(s):
    """Remove comments from a multi-statement sql block
    Parameters
    ----------
    statement : str
        The multi-statement SQL block
    Returns
    -------
    list
        Parsed sql statements 
    """
    
    NORMAL = 1
    COMMENT = 2
    QUOTE = 3
    BLOCK_COMMENT = 4

    output = []
    statement = ""
    mode = NORMAL

    for i, c in enumerate(s):
        if mode == COMMENT:
            if c == "\n":
                mode = NORMAL
                statement += " "
        elif mode == BLOCK_COMMENT:
            if c == "/" and i > 0 and s[i-1] == "*":
                mode = NORMAL
        elif mode == QUOTE:
            if c == "'":
                mode = NORMAL
            statement += c
        elif c == "'":
            mode = QUOTE
            statement += c
        elif c == ";":
            output.append(statement.strip())
            statement = ""
        elif c == "-" and i + 1 < len(s) and s[i+1] == "-":
            mode = COMMENT
        elif c == "/" and i + 1 < len(s) and s[i+1] == "*":
            mode = BLOCK_COMMENT
        elif c == "\n" or c == "\r":
            statement += " "
        else:
            statement += c.upper()
    
    statement = statement.strip()
    if statement:
        output.append(statement)
        
    return output

def statement_type(s):
    """Return the SQL statement type
    Parameters
    ----------
    statement : str
        Statement type
    -------
    str
        Type of SQL statement
    """
    if s.startswith('CREATE'):
        return 'CREATE'
    elif s.startswith('ALTER'):
        return 'ALTER'
    elif s.startswith('INS'):
        return 'INSERT'
    elif s.startswith('SEL'):
        return 'SELECT'
    elif s.startswith('UPDATE'):
        return 'UPDATE'
    elif s.startswith('DEL'):
        return 'DELETE'
    elif s.startswith('DROP'):
        return 'DROP'
    elif s.startswith('GRANT'):
        return 'GRANT'
    elif s.startswith('COLLECT'):
        return 'COLLECT'
    elif s.startswith('REPLACE'):
        return 'REPLACE VIEW'
    else:
        raise NotImplementedError

def remove_comments(statement):
    """Remove comments from a sql block.
    Parameters
    ----------
    statement : str
        The SQL statement
    Returns
    -------
    str
        Statement with comments discarded
    """
    blockless = statement
    block_start = blockless.find('/*')
    block_end = blockless.find('*/')
    while block_start > -1 and block_end > -1 and block_start < block_end:
        blockless = blockless[:block_start] + blockless[block_end + 2:]
        block_start = blockless.find('/*')
        block_end = blockless.find('*/')
    # parse out comment lines like --
    commentless = blockless
    comment_start = commentless.find('--')
    comment_end = commentless.find('\n', comment_start)
    while comment_start > -1 and comment_end > -1 and comment_start < comment_end:
        commentless = commentless[:comment_start] + commentless[comment_end + 1:]
        comment_start = commentless.find('--')
        comment_end = commentless.find('\n', comment_start)

    return commentless

def statement_split(statement):
    """Split a multi-statement SQL block into some chunks., and remove 
    comments.
    """
    # separate statements, keeping in mind possible semi-colons in strings
    cur_quote = None
    statement_lst = []
    cur_statement = ""

    for char in statement:
        cur_statement = cur_statement + char
        if cur_quote is None:
            if char in ('"', "'"):
                cur_quote = char
            elif char == ';':
                statement_lst.append(cur_statement.strip())
                cur_statement = ""
        else:
            if char == cur_quote:
                cur_quote = None
    statement_lst.append(cur_statement.strip())

    return [statement for statement in statement_lst if statement != '']
