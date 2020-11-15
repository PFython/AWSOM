![Amazing Ways to Search and Organise Media](https://github.com/PFython/AWSOMdesktop/blob/main/logo.png)

## 1. OVERVIEW

`AWSOMdesktop` is a collection of automation tools written in Python and
originally developed by Peter Fison (https://github.com/PFython) for use
at South West London TV Ltd as part of their Adobe Creative Cloud video
production workflow.

These desktop tools are part of a larger suite of apps collectively known as
"AWSOM" collection which stands for:

**A**mazing **W**ays to **S**earch and **O**rganise **M**edia.

which includes powerful tools for managing online media and is intended for
YouTuber channel owners and power-users of online video (not just YouTube) such
as journalists, researchers, and teachers.

This package contains a mixture of OS-independent Python scripts for managing
common automation tasks such as renaming media files and making backups, as well
as some exciting autiomations based on the superb `Pymiere` library by
Quentin Masingarbe (https://github.com/qmasingarbe/pymiere).  Unfortunately
`Pymiere` currently only supports Window 10, so those automations are limited
to Windows users for now.


 and are offered under the same GNU license as Pymiere itself.  Feel free to use and
enjoy, and perhaps support the project by sharing your own creations (and
tests, please) by forking Pymiere on Github and creating a Pull Request?



"AWSOM"   If you're interested in exploring the rest of the AWSOM toolkit, they'll be made
available via a snazzy new web app very soon hopefully - mostly free, but some
on a pay per use basis where we utilise third party services like professional
quality Automatic Speech Recognition.

In the meantime though, please follow us on Twitter and strike up a conversation!

https://twitter.com/AppAwsom

## 2. INSTALLATION

Very lightweight with only two dependencies (`cleverdict` and `pymiere`):

    pip install AWSOMdesktop

or to cover all bases...

    python -m pip install AWSOMdesktop --upgrade --user

## 3. BASIC USE

## 10. UNDER THE BONNET

`AWSOMdesktop` makes use of `CleverDict`, a handy custom data type which allows
developers to flexibly switch between Python dictionary `{key: value}` notation
and `object.attribute` notation.  For more information about `CleverDict` see:
https://pypi.org/project/cleverdict/

## 11. CONTRIBUTING

## 12. CREDITS

