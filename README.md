Last login: Sat Sep  6 19:26:20 on console
(base) sakthi@Sakthis-MacBook-Air ~ % git --version
git version 2.39.5 (Apple Git-154)
(base) sakthi@Sakthis-MacBook-Air ~ % cd path/to/leetcode-90days
cd: no such file or directory: path/to/leetcode-90days
(base) sakthi@Sakthis-MacBook-Air ~ % 
(base) sakthi@Sakthis-MacBook-Air ~ % cd path/to//Users/sakthi/Library/CloudStorage/GoogleDrive-sakthibala7531@gmail.com/My Drive/Leetcode/leetcode-90days
cd: string not in pwd: path/to//Users/sakthi/Library/CloudStorage/GoogleDrive-sakthibala7531@gmail.com/My
(base) sakthi@Sakthis-MacBook-Air ~ % cd "/Users/sakthi/Library/CloudStorage/GoogleDrive-sakthibala7531@gmail.com/My Drive/Leetcode/leetcode-90days"
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git init
Initialized empty Git repository in /Users/sakthi/Library/CloudStorage/GoogleDrive-sakthibala7531@gmail.com/My Drive/Leetcode/leetcode-90days/.git/
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git remote add origin https://github.com/SakthivelVinayagam/leetcode-90days.git
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git add .
git commit -m "Initial commit: LeetCode 90-Day Roadmap starter repo"
[main (root-commit) ed5e972] Initial commit: LeetCode 90-Day Roadmap starter repo
 Committer: Sakthi <sakthi@Sakthis-MacBook-Air.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 6 files changed, 59 insertions(+)
 create mode 100644 .DS_Store
 create mode 100644 Day01_TwoSum/notes.md
 create mode 100644 Day01_TwoSum/solution.py
 create mode 100644 Day02_BestTimeToBuySellStock/notes.md
 create mode 100644 Day02_BestTimeToBuySellStock/solution.py
 create mode 100644 README.md
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git branch -M main
git push -u origin main
Username for 'https://github.com': SakthivelVinayagam
Password for 'https://SakthivelVinayagam@github.com': 
remote: Permission to SakthivelVinayagam/leetcode-90days.git denied to SakthivelVinayagam.
fatal: unable to access 'https://github.com/SakthivelVinayagam/leetcode-90days.git/': The requested URL returned error: 403
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git credential-osxkeychain erase
host=github.com
protocol=https
git push -u origin main
bad input: git push -u origin main
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git push -u origin main
Username for 'https://github.com': SakthivelVinayagam
Password for 'https://SakthivelVinayagam@github.com': 
remote: Permission to SakthivelVinayagam/leetcode-90days.git denied to SakthivelVinayagam.
fatal: unable to access 'https://github.com/SakthivelVinayagam/leetcode-90days.git/': The requested URL returned error: 403
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git push -u origin main
Username for 'https://github.com': SakthivelVinayagam
Password for 'https://SakthivelVinayagam@github.com': 
remote: Permission to SakthivelVinayagam/leetcode-90days.git denied to SakthivelVinayagam.
fatal: unable to access 'https://github.com/SakthivelVinayagam/leetcode-90days.git/': The requested URL returned error: 403
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % printf "protocol=https\nhost=github.com\n" | git credential-osxkeychain erase
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git push -u origin main
Username for 'https://github.com': SakthivelVinayagam
Password for 'https://SakthivelVinayagam@github.com': 
remote: Permission to SakthivelVinayagam/leetcode-90days.git denied to SakthivelVinayagam.
fatal: unable to access 'https://github.com/SakthivelVinayagam/leetcode-90days.git/': The requested URL returned error: 403
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git push -u origin main
Username for 'https://github.com': SakthivelVinayagam               
Password for 'https://SakthivelVinayagam@github.com': 
remote: Permission to SakthivelVinayagam/leetcode-90days.git denied to SakthivelVinayagam.
fatal: unable to access 'https://github.com/SakthivelVinayagam/leetcode-90days.git/': The requested URL returned error: 403
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git remote -v
origin	https://github.com/SakthivelVinayagam/leetcode-90days.git (fetch)
origin	https://github.com/SakthivelVinayagam/leetcode-90days.git (push)
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % ssh-keygen -t ed25519 -C "sakthibala7531@gmail.com"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/sakthi/.ssh/id_ed25519): 
Enter passphrase for "/Users/sakthi/.ssh/id_ed25519" (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /Users/sakthi/.ssh/id_ed25519
Your public key has been saved in /Users/sakthi/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:AI0ZAtnlOSBTY7PS9w9vpDGKC6pmn6FPKoyxY/5d6C4 sakthibala7531@gmail.com
The key's randomart image is:
+--[ED25519 256]--+
|+=B.+=           |
|.=.Boo.          |
|. o = .          |
| . . o .         |
|      = S        |
|.  . ..O         |
|+o.o....+        |
|**+E= ..         |
|X===o+           |
+----[SHA256]-----+
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % eval "$(ssh-agent -s)"
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
Agent pid 37743
Enter passphrase for /Users/sakthi/.ssh/id_ed25519: 
Identity added: /Users/sakthi/.ssh/id_ed25519 (sakthibala7531@gmail.com)
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % mkdir -p ~/.ssh
cat >> ~/.ssh/config << 'EOF'
Host github.com
  HostName github.com
  UseKeychain yes
  AddKeysToAgent yes
  IdentityFile ~/.ssh/id_ed25519
EOF
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % pbcopy < ~/.ssh/id_ed25519.pub
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % pbcopy < ~/.ssh/id_ed25519.pub
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % ssh -T git@github.com
The authenticity of host 'github.com (64:ff9b::141a:9cd7)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
Hi SakthivelVinayagam! You've successfully authenticated, but GitHub does not provide shell access.
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % # From your leetcode-90days folder
git remote set-url origin git@github.com:SakthivelVinayagam/leetcode-90days.git
git push -u origin main
zsh: command not found: #
To github.com:SakthivelVinayagam/leetcode-90days.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'github.com:SakthivelVinayagam/leetcode-90days.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git remote set-url origin git@github.com:SakthivelVinayagam/leetcode-90days.git
git push -u origin main
To github.com:SakthivelVinayagam/leetcode-90days.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'github.com:SakthivelVinayagam/leetcode-90days.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git fetch origin main      
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 962 bytes | 192.00 KiB/s, done.
From github.com:SakthivelVinayagam/leetcode-90days
 * branch            main       -> FETCH_HEAD
 * [new branch]      main       -> origin/main
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git rebase origin/main
Auto-merging README.md
CONFLICT (add/add): Merge conflict in README.md
error: could not apply ed5e972... Initial commit: LeetCode 90-Day Roadmap starter repo
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply ed5e972... Initial commit: LeetCode 90-Day Roadmap starter repo
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git checkout --theirs README.md
Updated 1 path from the index
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git add README.md
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git rebase --continue
[detached HEAD 374b800] Initial commit: LeetCode 90-Day Roadmap starter repo
 Committer: Sakthi <sakthi@Sakthis-MacBook-Air.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 6 files changed, 31 insertions(+), 2 deletions(-)
 create mode 100644 .DS_Store
 create mode 100644 Day01_TwoSum/notes.md
 create mode 100644 Day01_TwoSum/solution.py
 create mode 100644 Day02_BestTimeToBuySellStock/notes.md
 create mode 100644 Day02_BestTimeToBuySellStock/solution.py
 delete mode 100644 README.md
Successfully rebased and updated refs/heads/main.
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git rebase --continue --no-edit
error: unknown option `no-edit'
usage: git rebase [-i] [options] [--exec <cmd>] [--onto <newbase> | --keep-base] [<upstream> [<branch>]]
   or: git rebase [-i] [options] [--exec <cmd>] [--onto <newbase>] --root [<branch>]
   or: git rebase --continue | --abort | --skip | --edit-todo

    --onto <revision>     rebase onto given branch instead of upstream
    --keep-base           use the merge-base of upstream and branch as the current base
    --no-verify           allow pre-rebase hook to run
    -q, --quiet           be quiet. implies --no-stat
    -v, --verbose         display a diffstat of what changed upstream
    -n, --no-stat         do not show diffstat of what changed upstream
    --signoff             add a Signed-off-by trailer to each commit
    --committer-date-is-author-date
                          make committer date match author date
    --reset-author-date   ignore author date and use current date
    -C <n>                passed to 'git apply'
    --ignore-whitespace   ignore changes in whitespace
    --whitespace <action>
                          passed to 'git apply'
    -f, --force-rebase    cherry-pick all commits, even if unchanged
    --no-ff               cherry-pick all commits, even if unchanged
    --continue            continue
    --skip                skip current patch and continue
    --abort               abort and check out the original branch
    --quit                abort but keep HEAD where it is
    --edit-todo           edit the todo list during an interactive rebase
    --show-current-patch  show the patch file being applied or merged
    --apply               use apply strategies to rebase
    -m, --merge           use merging strategies to rebase
    -i, --interactive     let the user edit the list of commits to rebase
    --rerere-autoupdate   update the index with reused conflict resolution if possible
    --empty <{drop,keep,ask}>
                          how to handle commits that become empty
    --autosquash          move commits that begin with squash!/fixup! under -i
    --update-refs         update branches that point to commits that are being rebased
    -S, --gpg-sign[=<key-id>]
                          GPG-sign commits
    --autostash           automatically stash/stash pop before and after
    -x, --exec <exec>     add exec lines after each commit of the editable list
    -r, --rebase-merges[=<mode>]
                          try to rebase merges instead of skipping them
    --fork-point          use 'merge-base --fork-point' to refine upstream
    -s, --strategy <strategy>
                          use the given merge strategy
    -X, --strategy-option <option>
                          pass the argument through to the merge strategy
    --root                rebase all reachable commits up to the root(s)
    --reschedule-failed-exec
                          automatically re-schedule any `exec` that fails
    --reapply-cherry-picks
                          apply all changes, even those already present upstream

(base) sakthi@Sakthis-MacBook-Air leetcode-90days % git status
git push -u origin main
On branch main
nothing to commit, working tree clean
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 8 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (9/9), 1.47 KiB | 1.47 MiB/s, done.
Total 9 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:SakthivelVinayagam/leetcode-90days.git
   aed6a78..374b800  main -> main
branch 'main' set up to track 'origin/main'.
(base) sakthi@Sakthis-MacBook-Air leetcode-90days % 
