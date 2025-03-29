document.addEventListener('DOMContentLoaded', function() {
    const userForm = document.getElementById('user-form');
    const userList = document.getElementById('user-list');

    userForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(userForm);
        const userData = {
            name: formData.get('name'),
            age: formData.get('age')
        };

        fetch('/add_user', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                addUserToList(data.user);
                userForm.reset();
            } else {
                alert('Error adding user');
            }
        });
    });

    function addUserToList(user) {
        const listItem = document.createElement('li');
        listItem.textContent = `${user.name} (${user.age} years old)`;
        userList.appendChild(listItem);
    }

    // Function to fetch and display users
    function fetchUsers() {
        fetch('/get_users')
            .then(response => response.json())
            .then(data => {
                data.users.forEach(user => {
                    addUserToList(user);
                });
            });
    }

    fetchUsers();
});