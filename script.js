// Atualiza o estado dos botões "Excluir" com base no número de elementos
function updateRemoveButtons() {
    const removeButtons = document.querySelectorAll('.element-row .btn-danger');
    const elementRows = document.querySelectorAll('.element-row');
  
    if (elementRows.length <= 1) {
        removeButtons.forEach(button => button.disabled = true);
    } else {
        removeButtons.forEach(button => button.disabled = false);
        elementRows[0].querySelector('.btn-danger').disabled = false; // Habilita o primeiro botão
    }
  }
  
  // Adiciona um novo elemento à lista
  function addElement() {
    const elementsDiv = document.getElementById('elements');
    const elementRow = createElementRow();
    elementsDiv.appendChild(elementRow);
    updateRemoveButtons();
  }
  
  // Cria uma nova linha de entrada de elemento com botão de exclusão
  function createElementRow() {
    const elementRow = document.createElement('div');
    elementRow.className = 'element-row';
  
    const newInput = document.createElement('input');
    newInput.type = 'text';
    newInput.className = 'element form-control element-input';
    newInput.placeholder = 'Informe um elemento da sua história...';
  
    const removeButton = document.createElement('button');
    removeButton.className = 'btn-danger';
    removeButton.innerText = 'Excluir';
    removeButton.onclick = () => removeElement(removeButton);
  
    elementRow.appendChild(newInput);
    elementRow.appendChild(removeButton);
  
    return elementRow;
  }
  
  // Remove uma linha de elemento
  function removeElement(button) {
    const elementRow = button.parentElement;
    elementRow.remove();
    updateRemoveButtons();
  }
  
  // Envia o formulário e gera a história
  async function submitForm() {
    const elementInputs = document.getElementsByClassName('element-input');
    const elementos = [];
  
    for (let i = 0; i < elementInputs.length; i++) {
        if (elementInputs[i].value) {
            elementos.push(elementInputs[i].value);
        }
    }
  
    if (elementos.length < 1) { // Alterado para exigir pelo menos um elemento
        alert('Por favor, informe pelo menos um elemento!');
        return;
    }
  
    const data = {
        elementos
    };
  
    try {
        const response = await fetch('http://127.0.0.1:5000/historia', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
  
        const result = await response.json();
        const responseDiv = document.getElementById('response');
  
        if (result) {
            const historia = result.join('')
            responseDiv.innerHTML = `<div>${historia}</div>`;
        } else {
            responseDiv.innerHTML = `<p>Erro: ${result.Erro}</p>`;
        }
  
        responseDiv.style.display = 'block';
    } catch (error) {
        const responseDiv = document.getElementById('response');
        responseDiv.innerHTML = `<p>Erro: ${error.message}</p>`;
        responseDiv.style.display = 'block';
    }
  }
  
  // Atualiza o estado dos botões "Excluir" quando o DOM é carregado
  document.addEventListener('DOMContentLoaded', updateRemoveButtons);
  
    
    