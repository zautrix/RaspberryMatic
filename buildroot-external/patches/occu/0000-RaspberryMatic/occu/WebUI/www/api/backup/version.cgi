##
# rfd-config
##
source common.tcl
proc main { } {
 puts "Content-Type: text/plain"
 puts ""
 puts -nonewline [loadFile /VERSION]
}

startup
