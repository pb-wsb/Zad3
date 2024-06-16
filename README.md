<h2>main.py</h2>
Simple script for testing swapi.dev api

<h2>app.py</h2>
Flask app - run it using <strong>py app.py</strong>
2 routes:
<ol>
    <li>/home - returns 'Hello world'</li>
    <li>/test - makes request to https://swapi.dev/api/test/<ppl_id>, where ppl_id is integer - example /test/1</li>
</ol>


<h2>Tests</h2>
Run tests using <strong>pytest</strong> command

<h2>Makefile</h2>
Commends:
<ol>
    <li><strong> make install</strong> - Installs dependencies from requirements.txt</li>
    <li><strong> make test</strong> - Run tests</li>
    <li><strong> make run</strong> - Runs application</li>
</ol>