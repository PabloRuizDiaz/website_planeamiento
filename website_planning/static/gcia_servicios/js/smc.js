function ExportToExcelTemplate(type, fn, dl) {
  var elt = document.querySelector('.tablaTemplate');
  var wb = XLSX.utils.table_to_book(elt, { sheet: "sheet1" });
  return dl ?
    XLSX.write(wb, { bookType: type, bookSST: true, type: 'base64' }):
    XLSX.writeFile(wb, fn || ('TemplateSitiosSMC.' + (type || 'xlsx')));
}

function ExportToExcelSitios(type, fn, dl) {
    var elt = document.querySelector('.tablasitios');
    var wb = XLSX.utils.table_to_book(elt, { sheet: "sheet1" });
    return dl ?
      XLSX.write(wb, { bookType: type, bookSST: true, type: 'base64' }):
      XLSX.writeFile(wb, fn || ('ResultadosSitiosSMC.' + (type || 'xlsx')));
 }

 function ExportToExcelCeldas(type, fn, dl) {
  var elt = document.querySelector('.tablaceldas');
  var wb = XLSX.utils.table_to_book(elt, { sheet: "sheet1" });
  return dl ?
    XLSX.write(wb, { bookType: type, bookSST: true, type: 'base64' }):
    XLSX.writeFile(wb, fn || ('ResultadosCeldasSMC.' + (type || 'xlsx')));
}