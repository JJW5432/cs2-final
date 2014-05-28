#!/bin/bash
name='devlog'
echo -e "#!/bin/bash\ngit log > ./"$name".txt\ngit add "$name".txt" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
