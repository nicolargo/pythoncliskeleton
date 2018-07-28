Skeleton
========

My Python CLI package skeleton... Compatible with Pypi repository ;)

How to use it ?
===============

Clone it:

    git clone git@github.com:nicolargo/pythoncliskeleton.git

Rename it to your *foo* project...

    mv pythoncliskeleton foo
    cd foo
    rm -rf .git
    mv skeleton foo
    find . -type f | xargs sed -i  's/skeleton/foo/g'
    find . -type f | xargs sed -i  's/Skeleton/Foo/g'
    echo "# Amazing Foo project" > ./README.rst
    echo "$(whoami)" > ./AUTHORS

Your skeleton is ready to be used !
