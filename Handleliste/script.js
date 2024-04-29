//alt av javascripten er skrevet med ChatGPT
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('shopping-form');
    const itemList = document.getElementById('items-list');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        addItem();
    });

    function addItem() {
        const itemInput = document.getElementById('item-input');
        const itemName = itemInput.value.trim();

        if (itemName !== '') {
            const li = document.createElement('li');
            li.textContent = itemName;

            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.addEventListener('change', function() {
                if (checkbox.checked) {
                    li.classList.add('completed');
                } else {
                    li.classList.remove('completed');
                }
            });

            const removeBtn = document.createElement('button');
            removeBtn.textContent = 'Remove';
            removeBtn.addEventListener('click', function() {
                li.remove();
            });

            li.appendChild(checkbox);
            li.appendChild(document.createTextNode(' '));
            li.appendChild(removeBtn);
            itemList.appendChild(li);

            itemInput.value = '';
            itemInput.focus();
        }
    }
});