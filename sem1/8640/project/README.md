<h1>RESTful APIs Project</h1>

<h2>Background</h2>
<p>Repository contains a basic RESTful API created within Python using Flask, to perform CRUD operations.</p>

<h2>Project Structure</h2>
<ol>
    <li><em>instance</em> directory: Contains the DB schema </li>
    <li><em>templates</em> directory: Contains index.html for the webpage</li>
    <li><strong>app.py</strong>: Python script which carries out the functionality. </li>
</ol>

<h2>Testing the application</h2>
<ol>
    <li>Run export FLASK_APP=app.py to point the Flask application to our application.</li>
    <li>Run flask init-db to initialise the Databse.</li>
    <li>Run flask run to run the application.</li>
    <li>Go to http://127.0.0.1:5000/? to test the application </li>
    <li>Add an item</li>
    <li>Test POST to Create a new item: curl -X POST -H "Content-Type: application/json" -d '{"name":"item1", "description":"desc1"}' http://127.0.0.1:5000/api/items </li>
    <li>Test GET to verify we are able to Read items: curl http://127.0.0.1:5000/api/items </li>
    <li>Test PUT to verify we are able to Update items: curl -X PUT -H "Content-Type: application/json" -d '{"name":"New Name", "description":"New Description"}' http://127.0.0.1:5000/api/items/1</li>
    <li>Test DELETE to verify we are able to Delete items: curl -X DELETE http://127.0.0.1:5000/api/items/1 </li>
</ol>

<h2>Room for improvement (aka "What I'd do if I had more time outside work/life commitments")</h2>
<ol>
    <li>Improve UI to show a table containing the data points, updating in real time.</li>
</ol>