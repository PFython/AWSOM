![Amazing Ways to Search and Organise Media](https://raw.githubusercontent.com/PFython/AWSOM-PyPi/main/logo.png)

## 1. OVERVIEW

`AWSOM` stands for: **A**mazing **W**ays to **S**earch and **O**rganise
**M**edia.  `AWSOM` is a media automation toolkit, originally intended to
automate the Adobe Creative Cloud video production workflow at
[South West London TV](https://www.southwestlondon.tv).

This Python package contains a mixture of OS-independent scripts for managing
common (desktop/LAN) automation tasks such as renaming media files and making backups, as well
as some exciting automations built on top of the superb `Pymiere` library by
[Quentin Masingarbe](https://github.com/qmasingarbe/pymiere).  Unfortunately
`Pymiere` currently only works on **Windows 10**, so the corresponding `AWSOM`
automations are limited to Windows users as well (for now).

If you're interested in exploring the rest of the **AWSOM** toolkit, which is
primarily aimed at serious YouTubers, video editors, and power-users of online
video such as journalists, researchers, and teachers, please follow us on Twitter
and start a conversation:

![Follow us on Twitter](https://cdn.exclaimer.com/Handbook%20Images/twitter-icon_square_64x64.png?_ga=2.206957524.690480154.1605528377-685225211.1605528377)

https://twitter.com/AppAwsom

Both this package and a snazzy new web version of `AWSOM` which we hope to launch soon provide a
tonne of powerful features completely free, but certain 'Pro' features like
Automatic Speech Recognition/Subtitling use third party services and may require
a registered account with us or them to access on a pay-per-use basis.


## 2. INSTALLATION

Very lightweight with only two dependencies: `cleverdict` and `pymiere`.

    pip install AWSOM

or to cover all bases...

    python -m pip install AWSOM --upgrade --user

## 3. BASIC USE
`AWSOM` currently supports Sony's commonly used XDCAM format.  More formats will be added soon, or feel free to get involved and contribute one!

1. Connect and power on your camera/storage device

    ```
    import AWSOM
    AWSOM.ingest(from_device=True)
    ```
2. Follow the (beautiful `PySimpleGui`) prompts to give your project a name and category/prefix, and point it to a template `.prproj` file to copy from.

   ![](https://raw.githubusercontent.com/PFython/AWSOM/main/popup1.png)
   
   ![](https://raw.githubusercontent.com/PFython/AWSOM/main/popup2.png)
   
   ![](https://raw.githubusercontent.com/PFython/AWSOM/main/popup3.png)

3. Go and have a cup of coffee, knowing that when you come back all the fiddly, non-creative, importy-draggy stuff will be done and you can get on with *actual* editing!
   * New project Folder created on your main work hard drive.
   * All media and metadata copied to subfolder `XDROOT`.
   * All clips, thumbnails and XML files renamed to include the project name.
   * `MEDIAPRO.XML` updated with new names.
   * Your selected template .prproj file opened in Premiere Pro.
   * Template file save with new project name to new folder.
   * Rushes bin created if not already in the template.
   * All clips imported into the Rushes bin.
   * Rushes sequence created if not already in the template.
   * All clips inserted in the Rushes sequence, all ready and waiting for you!

## 4. UNDER THE BONNET

None of `AWSOM`'s automations for `Adobe Premiere Pro` would be possible without `Pymiere`.

`AWSOM`'s library of choice for user interaction is `PySimpleGui` which creates beautiful looking popups, input windows and output displays with very few lines of code.  We think their documentation is really fun and accessible too which makes the learning-curve for newcomers really painless.


Internally, `AWSOM` makes extensive use of `CleverDict`, a handy custom data type which allows
developers to flexibly switch between Python dictionary `{key: value}` notation
and `object.attribute` notation.  For more information about `CleverDict` see:
https://pypi.org/project/cleverdict/

`AWSOM` uses `pathlib` in preference to `os` wherever possible for handling files, directories, and drives.

The primary class used in `AWSOM` is `Project` which encapsulates all the control data used by the rest of the main program.

Functions and methods are generally as 'atomic' as possible, i.e. one function generally does just one thing and is kept as short as reasonably possible.  The exception to this are *workflow functions* like `ingest()` which by their nature chain together potentially long sequences of individual functions, passing a `Project` object between them.



## 5. CONTRIBUTING

Please join our virtual team if you have an interest in video editing, production, workflow automation or simply have an idea for improving this package.  We're particularly keen to connect with anyone who can help us make `Pymiere` work on other Operating Systems and folk already active in the Adobe/Premiere/ExtendScript space or working on tools for Speech Recognition, Subtitles, Media Content Management, and online video generally (especially but not only YouTube).  We're also on the lookout for professional help with UX/UI design and all things HTML/CSS to take our web app version of `AWSOM` to the next level.

Our preferred process for onboarding new contributors is as follows:

1. Say hello to us on [Twitter](https://twitter.com/AppAwsom) initially so we can "put a face to the name".
2. Fork this repository.  Also **STAR** this repository for bonus karma!
3. Create new branches with the following standardised names as required:
   * `cosmetic`: for reformatting and changes to comments, README, or user input/output e.g. print(), input() and GUI.
   * `enhancements`: for new features and extensions to old features
   * `refactoring`: for better ways to code existing features
   * `tests`: for new or better test cases
   * `bugfix`: for solutions to existing issues
   * `miscellaneous`: for anything else
4. We're a naively zealous fan of *Test Driven Development*, so please start by creating a separate `test_xyz.py` script for any coding changes, and document your tests (and any new code) clearly enough that they'll tell us everything we need to know about your rationale and implementation approach.
5. When you're ready and any new code passes all your/our tests, create a *Pull Request* from one of your branches (above) back to the `main` branch of this repository.

If you'd be kind enough to follow that approach it will speed things on their way and cause less brain-ache for us, thanks!


