#!/bin/sh

### Configuration section ###

TITLE="<h2 style=\"color: green; font-size: 46px;\">These are the Fossil Repositories of dastagg.</h2>"
FOSSIL=/usr/local/bin/fossil
REPOSROOT=/var/www/fossils
REPOSEXT=".fsl"

### Processing section -- nothing to configure here! ###

set -f    ; # disable filename globbing

## Some helper functions

HeaderText () {
  if [ -z "$headerWritten" ]; then
    echo "Content-type: text/plain; charset=iso-8859-1"
    echo
    headerWritten=1
  fi
}

HeaderHTML () {
  if [ -z "$headerWritten" ]; then
    echo "Content-type: text/html; charset=iso-8859-1"
    echo
    headerWritten=1
  fi
}

Error () {
  HeaderHTML
  echo "<p><font color="red">ERROR: $1</font></p>"
  exit 1
}

P () {
  HeaderText
  for var in $*; do
    eval echo $var = "\$$var"
  done
}

## Do the real work here ...

project=`echo $PATH_INFO | sed -e 's!/\([^/]*\).*!\1!'| tr "[A-Z]" "[a-z]"`
repos="$REPOSROOT/$project$REPOSEXT"

if [ -r "$repos" ]; then
  PATH_INFO=`echo $REQUEST_URI | sed -e "s!^$SCRIPT_NAME/$project\\([^?]*\\).*!\\1!"`
  : ${PATH_INFO:=/}
  SCRIPT_NAME=$SCRIPT_NAME/$project
  TEMPFILE=`mktemp /tmp/fossil-$project.XXXXXX` || Error "Couldn't create tempfile"
  trap "rm -f $TEMPFILE" EXIT QUIT INT TERM
  echo repository: $repos > $TEMPFILE
  $FOSSIL cgi $TEMPFILE
elif [ -z "$project" ]; then
  HeaderHTML
  echo "$TITLE"
  echo "<ul>"
  find $REPOSROOT -name "*$REPOSEXT" | sort | \
  while read repos; do
    project=`basename $repos $REPOSEXT`
    if [ -f $repos -a ! -e $REPOSROOT/.$project ]; then
      echo "<li style=\"font-size: 28px;\"><a href='${REQUEST_URI}$project'>$project</a></li>"
    fi
  done
  echo "</ul>"
else
  Error "No such project: $project"
fi

exit 0


