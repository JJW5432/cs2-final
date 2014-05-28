#!/bin/bash
name='devlog'
echo -e "#!/bin/bash\ngit log > ~/cs2-final/"$name".txt\ngit add "$name".txt" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
