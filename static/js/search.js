$(document).ready(function() {
    var table = $('#main_table').DataTable();

    $('input.column_search').on('keyup change', function() {
        var columnIndex = $(this).data('column-index');
        table.column(columnIndex).search(this.value).draw();
    });
});

