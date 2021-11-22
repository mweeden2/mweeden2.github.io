#!/bin/bash


#  Grab the poem's title
# ---------------------------------------
title=$(head -n 1 $1)

#  Set up html template
# ---------------------------------------
poem_template=$"<!DOCTYPE html>
<html>
    <head>
        <link rel=\"stylesheet\" href=\"index.css\">
        <link rel=\"stylesheet\" href=\"poetry.css\">
    </head>
    <body>
        <span><a href=\"index.html\">home</a> / $title</span>
        <h3>$title</h3>
            <p>
                $title
            </p>
    </body>
</html>"

echo -e $poem_template


#  Grab each paragraph in the poem
# ---------------------------------------


    #  Grab each line in the paragraph
    # ---------------------------------------
