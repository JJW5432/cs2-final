#!/bin/bash
echo -e "#!/bin/bash\ngit log > ~/cs2-final/log.txt\ngit add log.txt" > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
