#!/bin/bash
name='devlog'
echo -e "#!/bin/bash\ngit log > ./"$name".txt" > .git/hooks/post-commit
chmod +x .git/hooks/post-commit
