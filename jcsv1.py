import streamlit as st

# JavaScript code snippets
js_objects = """
// Basic object
let person = {
  firstName: "John",
  lastName: "Doe",
  age: 30,
  job: "Developer",
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
};

// Nested object
let company = {
  name: "Tech Corp",
  address: {
    street: "123 Main St",
    city: "Anytown",
    state: "CA",
    zip: "12345"
  },
  employees: ["Alice", "Bob", "Charlie"]
};

// Object with methods
let calculator = {
  add: function(a, b) {
    return a + b;
  },
  subtract: function(a, b) {
    return a - b;
  },
  multiply: function(a, b) {
    return a * b;
  },
  divide: function(a, b) {
    return a / b;
  }
};
"""

js_variables = """
// Variable declaration
let greeting = "Hello, world!";
const pi = 3.14159;
var count = 42;

// Array
let numbers = [1, 2, 3, 4, 5];

// Function
function sayHello(name) {
  return `Hello, ${name}!`;
}

// Arrow function
const addNumbers = (a, b) => a + b;
"""

js_json_objects = """
// Basic JSON object
{
  "firstName": "Jane",
  "lastName": "Doe",
  "age": 25,
  "email": "jane.doe@example.com"
}

// Nested JSON object
{
  "company": "Innovative Solutions",
  "location": {
    "address": "456 Elm St",
    "city": "Othertown",
    "state": "TX"
  },
  "departments": [
    "Engineering",
    "Marketing",
    "Sales"
  ]
}

// JSON array
[
  {
    "name": "Product A",
    "price": 29.99
  },
  {
    "name": "Product B",
    "price": 39.99
  }
]
"""

js_fetch_api = """
// GET request
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));

// POST request
fetch('https://api.example.com/data', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ key: 'value' })
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
"""

js_dom_manipulation = """
// Selecting elements
let heading = document.querySelector('h1');
let paragraphs = document.querySelectorAll('p');

// Modifying content
heading.textContent = "New Heading";
paragraphs.forEach(p => p.textContent = "New paragraph content");

// Adding event listeners
let button = document.querySelector('button');
button.addEventListener('click', () => alert('Button clicked!'));
"""

js_event_handling = """
// Event listener for button click
document.getElementById('myButton').addEventListener('click', function() {
  alert('Button clicked!');
});

// Event delegation
document.body.addEventListener('click', function(event) {
  if (event.target.matches('.myClass')) {
    console.log('Element with class "myClass" clicked!');
  }
});
"""

js_local_storage = """
// Set item
localStorage.setItem('username', 'JohnDoe');

// Get item
let username = localStorage.getItem('username');
console.log(username);

// Remove item
localStorage.removeItem('username');

// Clear all items
localStorage.clear();
"""

js_promises = """
// Creating a Promise
let myPromise = new Promise((resolve, reject) => {
  let success = true;
  if (success) {
    resolve('Promise resolved successfully!');
  } else {
    reject('Promise rejected.');
  }
});

// Consuming a Promise
myPromise.then(result => {
  console.log(result);
}).catch(error => {
  console.error(error);
});
"""

js_async_await = """
// Async function
async function fetchData() {
  try {
    let response = await fetch('https://api.example.com/data');
    let data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchData();
"""

st.title("JavaScript Snippets for Mobile App Connectivity")

st.write("### JavaScript Objects")
st.code(js_objects, language='javascript')
if st.button('Copy JavaScript Objects to Clipboard'):
    st.session_state.clipboard = js_objects

st.write("### JavaScript Variables")
st.code(js_variables, language='javascript')
if st.button('Copy JavaScript Variables to Clipboard'):
    st.session_state.clipboard = js_variables

st.write("### JSON Objects")
st.code(js_json_objects, language='javascript')
if st.button('Copy JSON Objects to Clipboard'):
    st.session_state.clipboard = js_json_objects

st.write("### Fetch API for AJAX Requests")
st.code(js_fetch_api, language='javascript')
if st.button('Copy Fetch API Code to Clipboard'):
    st.session_state.clipboard = js_fetch_api

st.write("### DOM Manipulation")
st.code(js_dom_manipulation, language='javascript')
if st.button('Copy DOM Manipulation Code to Clipboard'):
    st.session_state.clipboard = js_dom_manipulation

st.write("### Event Handling")
st.code(js_event_handling, language='javascript')
if st.button('Copy Event Handling Code to Clipboard'):
    st.session_state.clipboard = js_event_handling

st.write("### Local Storage")
st.code(js_local_storage, language='javascript')
if st.button('Copy Local Storage Code to Clipboard'):
    st.session_state.clipboard = js_local_storage

st.write("### Promises")
st.code(js_promises, language='javascript')
if st.button('Copy Promises Code to Clipboard'):
    st.session_state.clipboard = js_promises

st.write("### Async/Await")
st.code(js_async_await, language='javascript')
if st.button('Copy Async/Await Code to Clipboard'):
    st.session_state.clipboard = js_async_await

# Clipboard functionality (if using with Streamlit Server with custom JS)
st.markdown("""
<script>
function copyToClipboard(text) {
  const el = document.createElement('textarea');
  el.value = text;
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);
}

const buttons = document.querySelectorAll('button');
buttons.forEach((button, index) => {
  button.addEventListener('click', () => {
    if (window.streamlitCustomEvent) {
      const text = document.querySelectorAll('pre code')[index].innerText;
      window.streamlitCustomEvent({type: 'COPY', payload: text});
    }
  });
});
</script>
""", unsafe_allow_html=True)
