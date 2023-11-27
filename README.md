# FactorDB-cli
This tool can be used to access factordb (usually used in cryptograpy to obtain known factors of large numbers) from the terminal.
Uses python3 requests module to access website, and HTML-based parsing to obtain required factors.

To configure as a CLI command:
1.  Clone repo into any directory.
2.  Rename file to 'factordb' (just to give the feel of a CLI tool)
3.  Give required permissions to the file, and copy/move it to `/usr/local/bin`

NOTE : I am not entirely sure about the safety regarding copying a file into `/usr/local/bin`, so do it in general at your own risk.

*Alternate soln - You could create an alias in .bashrc to run the program (eg : `ALIAS factordb='python3 factordb.py'`)*
