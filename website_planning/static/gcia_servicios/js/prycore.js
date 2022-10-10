const buttomNuevoPry = document.querySelector('.buttomNuevoPry');
const nuevo_pry = document.querySelector('.nuevo_pry');

const buttomActPry = document.querySelector('.buttomActPry');
const actualizar_pry = document.querySelector('.actualizar_pry');

const buttomActEst = document.querySelector('.buttomActEst');
const actualizar_estado = document.querySelector('.actualizar_estado');

const buttomVerBusqueda = document.querySelector('.buttomVerBusqueda');
const verBusqueda = document.querySelector('.verBusqueda');


buttomNuevoPry.addEventListener('click', () => {
  if (nuevo_pry.style.display === 'none') {
    nuevo_pry.style.display = 'block';
    actualizar_pry.style.display = 'none';
    actualizar_estado.style.display = 'none';
    verBusqueda.style.display = 'none';
  } else {
    nuevo_pry.style.display = 'none';
    actualizar_pry.style.display = 'none';
    actualizar_estado.style.display = 'none';
    verBusqueda.style.display = 'none';
  }
})

buttomActPry.addEventListener('click', () => {
  if (actualizar_pry.style.display === 'none') {
    nuevo_pry.style.display = 'none';
    actualizar_pry.style.display = 'block';
    actualizar_estado.style.display = 'none';
    verBusqueda.style.display = 'none';
  } else {
    nuevo_pry.style.display = 'none';
    actualizar_pry.style.display = 'none';
    actualizar_estado.style.display = 'none';
    verBusqueda.style.display = 'none';
  }
})

buttomActEst.addEventListener('click', () => {
  if (actualizar_estado.style.display === 'none') {
    nuevo_pry.style.display = 'none';
    actualizar_pry.style.display = 'none';
    actualizar_estado.style.display = 'block';
    verBusqueda.style.display = 'none';
  } else {
    nuevo_pry.style.display = 'none';
    actualizar_pry.style.display = 'none';
    actualizar_estado.style.display = 'none';
    verBusqueda.style.display = 'none';
  }
})

buttomVerBusqueda.addEventListener('click', () => {
  if (verBusqueda.style.display === 'none') {
    nuevo_pry.style.display = 'none';
    actualizar_pry.style.display = 'none';
    actualizar_estado.style.display = 'none';
    verBusqueda.style.display = 'block';
  } else {
    nuevo_pry.style.display = 'none';
    actualizar_pry.style.display = 'none';
    actualizar_estado.style.display = 'none';
    verBusqueda.style.display = 'none';
  }
})


function findPry() {
  var input, filter, table, tr, td, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("tablapry");
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[3];
      if (td) {
          if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
              tr[i].style.display = "";
          } else {
              tr[i].style.display = "none";
          }
      }
  }
  
  table = document.getElementById("tablaestado");
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
          if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
              tr[i].style.display = "";
          } else {
              tr[i].style.display = "none";
          }
      }
  }
}
