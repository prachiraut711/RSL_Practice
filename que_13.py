# 16. Given a string check for balanced parenthasis if it is balanced then 
#    return string as it is otherwise balance it.

#    i/p - {{{}
#    o/p - {{{}}}

#    i/p - }{{}}{
#    o/p - {}{{}}{}

#    i/p - }}}
#    o/p - {{{}}}

#    i/p - {}}{{}
#    o/p - {{}}{{}}


def balance_braces(s):
    open_count = 0
    close_count = 0
    for i in s:
        if i == "{":
            open_count += 1
        elif i == "}":
            if open_count > 0:
                open_count -= 1
            else:                #mahnjech jevva open_count = 0 aseltar
                close_count += 1
        
    return "{" * close_count + s + "}" * open_count

print(balance_braces("{{{}"))     # {{{}}}
print(balance_braces("}{{}}{"))   # {}{{}}{}
print(balance_braces("}}}"))      # {{{}}}
print(balance_braces("{}}{{}"))   # {{}}{{}}


