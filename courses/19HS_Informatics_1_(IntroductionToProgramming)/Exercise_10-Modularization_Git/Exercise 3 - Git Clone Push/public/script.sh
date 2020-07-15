# Variables can either be defined and directly used...
SOME_VAR="Hello World!"
echo $SOME_VAR
git clone $REPO_URL repo
cd repo
printf "ccc" > c.txt
git add c.txt
git commit -m "Add new file c.txt with some content"
git push
