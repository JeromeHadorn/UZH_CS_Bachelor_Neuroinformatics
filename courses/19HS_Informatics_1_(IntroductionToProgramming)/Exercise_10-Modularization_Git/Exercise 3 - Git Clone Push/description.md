Git repositories are typically used to synchronize the work between different developers. In this task, we will test, if you know how to `clone` an existing repository and how to `push` your updates. You will again work in the script file `script.sh`. It is possible to use variables in the script, we will use `$REPO_URL` to point to the repository that you should clone.

For this task, perform the following steps:

* Clone the repository at `$REPO_URL` into the folder `repo`.
* Change the working directory to the new folder (using the command `cd`).
* Create a new file `c.txt` with the content `ccc`.
* Add and commit your changes using the message `Add new file c.txt with some content`.
* Push the new commit to the repository.

**Note:** After executing the script, your index should be clean and there should be no changed files in your working directory.

**Note:** Use `$REPO_URL` and do not change the folder name or the grading scipt will fail. If you want to test your script locally, you can provide an arbitrary Git repository URL when running the script, just execute the command `REPO_URL="http://some.server.com/yourname/yourrepo" ./script.sh`.

**Note:** Your scripts cannot access the internet and will timeout if you try.
