#!/usr/bin/env python

import re
string_list = []


def say(text):
    print "Say: '%s'" % text


func_dict = {'say':say}


script = """

# This is a comment
on_load()
    {
    test(10,20,30)
    # This is another comment
    say("Hello, World!", 30)     # and a third one comment
    }


on_aggro()
    {
    say("Time to die, ${name}!")
    anger("")
    }

on_hear("what pirates")
    {
    say("Well, let me tell #you# a yarn. Sit down and pull up that stool." )
    schedule("test",30)
    }

"""


#func_dict['say']("This is a test")


class Tokenizer(object):

    def __init__(self):

        pass


    def tokenize(self, script):

        self.string_list = []

        PSTR = '__PARAM_STR__'

        is_parenthetic = False
        is_quoted = False
        is_comment =False
        
        cur_string = ''
        pass1 = ''

        ## Error checking
        errors = []
        line = 1
        open_paren = -1
        open_quote = -1

        ## PASS ONE; remove comments and extract parameter strings

        for c in script:

            if c == '\n':
                line += 1

            ## are we in a comment?        
            if is_comment:

                ## Newline ends comment
                if c == "\n":
                    is_comment = False
                    pass1 += '\n'
           
            ## Are we inside a quote block?
            elif is_quoted:

                if c != '\"':
                    cur_string += c
                ## End quote block
                else:
                    is_quoted = False                    
    
            ## Begin comment block
            elif c == '#':
                is_comment = True

            ## Begin quote block
            elif c == '\"':
                open_quote = line
                is_quoted = True

            ## Are we inside parenthesis?
            elif is_parenthetic:
 
                ## end argument
                if c == ',':
                    self.string_list.append(cur_string)
                    pass1 += ' ' + PSTR
                    cur_string = ''
            
                ## End parenthetic block
                elif c == ')':
                    self.string_list.append(cur_string)
                    pass1 += ' ' + PSTR
                    cur_string = ''
                    is_parenthetic = False
 
                elif c == '(':
                    errors.append("Line %d: Unexpected opening '(' in source."
                        % line) 
   
                elif not c.isspace():
                    cur_string += c

            ## Begin parenthetic block
            elif c == '(':
                open_paren = line
                is_parenthetic = True

            ## Lastly, pass the character
            else:
                pass1 += c


        if is_quoted:
            errors.append("Line %d: Quotation is never closed by EOF." 
                % open_quote)

        if is_parenthetic:
            errors.append("Line %d: Parentheses are never closed by EOF." 
                % open_paren)



        print self.string_list
        print pass1
        print errors
      
        ## PASS TWO; build command tuples
              
        #for line_number, line in enumerate(pass1.split('\n')):
        #    print line_number, line.split()


if __name__ == '__main__':

    t = Tokenizer()

    t.tokenize(script)





