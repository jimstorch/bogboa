#Coloring Text Inline with Caret Codes

# Introduction #

In order to make text decorating easier, you can use the following caret codes inside blocks of text.  If the client has turned off color, the tokens are simply stripped out.

You'll notice there is a pattern to the codes which should be easy to remember -- lower case = dark/mode on, uppercase = bright/mode off.  Some, like Underline and Bold, unset using the opposite shift-state of same key.  Black is 'k' as in CMYK, since Blue took the 'b'.

# Caret Codes #
```

  ^k   = black
  ^K   = bold black (grey)
  ^r   = red
  ^R   = bold red
  ^g   = green
  ^G   = bold green
  ^y   = yellow
  ^Y   = bold yellow
  ^b   = blue
  ^B   = bold blue
  ^m   = magenta
  ^M   = bold magenta
  ^c   = cyan
  ^C   = bold cyan
  ^w   = white
  ^W   = bold white
  ^!   = bold on (use within a block of non-bright text)
  ^1   = bold off 
  ^d   = default (should be white text on black)    
  ^kb  = black background
  ^rb  = red background
  ^gb  = green background
  ^yb  = yellow background
  ^bb  = blue background
  ^mb  = magenta background
  ^cb  = cyan background
  ^i   = inverse text on  
  ^I   = inverse text off
  ^^   = reset all
  ^_   = (caret underbar) underline on
  ^-   = (caret minus) underline off

```

# Example #

The following would print in dim green with the word 'gold' bolded (brighter green) and 'Eugene Levy' in bright red text.  Then the text is reset to the terminal's default just before the exclamation point.

```
^gYou see a huge pile of ^!gold^1 guarded by ^REugene Levy^^!
```