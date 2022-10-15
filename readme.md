<h1>Details and Instructions</h1>	
<h2>Application</h2>

<h3>Modules</h3>
The <code>csc301a2</code> folder contains following modules:<br>
<strong>Frontend</strong><br> 
<code>style.css</code> Describes HTML display<br> 
<code>index.html</code> A webpage for UI<br> 
<code>Procfile</code> Required file for Heroku deployment. <br>
<code>requirent.txt</code> Required file for Heroku deployment.<br>
<code>.flaskenv</code> Required file for Flask <br>
<strong>Backend</strong><br>
<code>item.py</code> Class definition of <code>Item</code> that is in store.<br>
<code>counter.py</code> Class definition of <code>Counter</code> which is responsible for managing 
items in the shopping cart and checkout. <br>
<code>read_csv.py</code> Reads a list of available items in csv files into <code>Item</code> objects <br>
<code>app.py</code> Main function that user needs to run <br>
<code>test.py</code> Unit tests of main functions of the checkout machine <br> 
<code>item_list.csv</code> A csv file that contains information of items.<br>

<h3>Description</h3>

index.html is the HTML frontend and style.css is its style sheet. It contains some input textbox that can input the number and quantity of a product, and buttons that can add or delete product from the cart. It also contains a button to reset the cart and a button to show the invoice.

app.py initializes the counter and contains some Flask methods that handles the POST request sent from the frontend. It calls differnet backend methods based on the button that user clicked and sends data stored in the backend to the frontend.

Each <code>Item</code> object has 3 main attributes, which is a unique <em>id number</em>
associated with the item, the <em>price</em> of the item, and the <em>quantity</em> of that item. <br>
A <code>Counter</code> object has private attributes <em>instock</em> list that contains all items that
could be sold. Private attributes <em>cart</em> is a list of items that currently in the shopping 
cart. Method <code>set_tax</code> and <code>set_discount</code> allows user to set 
tax and discount for the current bill. <code>add_cart</code> and <code>remove_cart</code>
allow user to add and remove items by their associated id.  <code>calculate_total</code>
returns total value for the current cart.<br>
To sum up, store will prepare a list of items in stock (csv) &rarr; <code>read_csv.py</code> 
reads csv file into items &rarr; <code>Counter</code> manage items &lrarr; <code>run.py</code>
&lrarr; <code>index.html</code> interact with users and gets commands


<h2>Deployment</h2>
We use Heroku to deploy our project.
We used Heroku CLI to link to our Github and deploy the project. Webapplink: https://checkoutsonnycaules.herokuapp.com/


<h2>Testing Instructions</h2>

<strong>Requirement</strong>:<br> install <code>unittest</code> library for python unit testing. <br>
install <code>Flask</code> library for Python database.<br>
<strong>Instructions:</strong><br>
To test frontend UI, first, run <code>run.py</code> in Python console. Second, open the generated link in the console with your browser.<br>
Here is a demo video on how to use the program: https://1drv.ms/v/s!Aot4DPCd3yT-dzGF_AOlnbA9pAE?e=RItM5p <br>
In order to check backend functions, simply run <code>test.py</code> which contains 
unit tests that cover main functions.

