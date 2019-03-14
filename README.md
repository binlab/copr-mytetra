# Fedora COPR - MyTetra

[![Copr build status](https://copr.fedorainfracloud.org/coprs/binlab/mytetra/package/mytetra/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/binlab/mytetra/package/mytetra/)

__MyTetra__ is a full-featured, open source, cross-platform note 
manager (PIM-manager) used to collect and accumulate various 
kinds of information. All entries (notes, articles) are organized 
in a tree structure, as well as supplied with keywords tags that 
allow you to quickly find the right entries. Links between records, 
attachments, encryption, detailed search, synchronization, copying 
from the browser, one of the best visual WYSIWYG text editors - all 
this is in the PIM-manager MyTetra. It is powerful program for data 
memorization and structuring notes.

Features:
  * Infinite ramify tree for notes group
  * Arbitrary sorted notes at his branch
  * Arbitrary sorted branches at parent branch
  * Copy/Paste for notes and branches
  * Clickable tags
  * Customizable trash for recovery lost data
  * WYSIWYG editor
  * Notes encryption by RC5-32/12/16 + PBKDF2
  * Synchronization over any cloud storage system or version 
    control system (i.e. Git on GitHub.com)
  * History navigation
  * etc

### Links
---

* [Fedora COPR](https://copr.fedorainfracloud.org/coprs/binlab/mytetra/)
* [SPECs Repo](https://github.com/binlab/copr-mytetra)
* [MyTetra Sources](https://github.com/xintrea/mytetra_dev)
* [MyTetra Webpage](https://webhamster.ru/site/page/index/articles/projectcode/138)

### Installation
---

* On Fedora

    ```shell
    $ sudo dnf copr enable binlab/mytetra
    $ sudo dnf install mytetra
    ```

### How to use synchronization in MyTetra

---

To synchronize, you can use any of cloud storage or any version control system. The main thing is that these systems maintain atomicity. The author has tested and recomendet used `Git`.

To synchronize data, you simply synchronize the contents of the directory `/data`. To get path to directory `/data`, select `"Tools" -> "Preferences" -> "Main" -> "Data directory"` and click on the button with three dots [...].

First, create repository at `GitLab`, with name i.e. `mytetra`. At console, enter to directory `/data` and type command to upload files to your `GitLab` repository:

```shell
git init
git add .
git commit -a -m "Init commit"
git remote add origin git@github.com:username/mytetra.git
git push -u origin master
```
 
Next, select `"Tools" -> "Preferences" -> "Synchro"` and set syncro command:


* For Linux:

```shell
date=$(date --iso-8601=seconds) ; cd %a ; git add . ; git commit -am "Sync: $date" ; git pull -s recursive ; git push
```

* For Windows:
 
```shell
cd \ & cd "%a" & git add . & git commit -am "MyTetra Sync" & git pull -s recursive & git push
```

After these steps, you will have to work "back up data" to GitHub.com. Do not forget to pre-encrypt the items with private data: service GitHub keeps history of files.

_**Warning! At earlier in this command line was writed wrong option -X theirs. Please, remove this option from your synchro command line.**_

Next, install MyTetra to other computer. Find `/data` directory, and delete all from it. In `/data` directory run command:

```shell
git clone git@github.com:username/mytetra.git .
```

Run MyTetra, and next set synchro command (see up) to `"Tools" -> "Preferences" -> "Synchro"`