#!/bin/sh
tempfile="$(mktemp)"
trap 'rm -rf "${tempfile}"' EXIT
cat > "${tempfile}"
# modify ${tempfile}
cat "${tempfile}"

