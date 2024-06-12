(function($){
    $(document).ready(function(){

        /* datepicker */
        $('.suit-datepicker').datepicker({
            format: 'yyyy-mm-dd',
            autoclose: true,
            todayBtn: 'linked',
            todayHighlight: true,
        });

        /* datetimepicker */
        $('.suit-datetimepicker').datetimepicker({
            format: 'yyyy-mm-dd hh:ii',
            autoclose: true,
            todayBtn: 'linked',
            todayHighlight: true,
        });

        /* timepicker */
        $('.suit-timepicker').timepicker({
            minuteStep: 1,
            secondStep: 5,
            showInputs: false,
            showMeridian: false,
            defaultTime: false
        });

        /* richtext widget */
        if ($.fn.wysihtml5 !== undefined) {
            $('.suit-richtext').each(function(index, element){
                var height = $(element).attr('data-suit-richtext-height') || 400;
                $(element).wysihtml5({height: height});
            });
        }

        /* select2 */
        if ($.fn.select2 !== undefined) {
            $.fn.select2.defaults.dropdownCssClass = 'dropdown-inverse';
            $('.suit-select').select2();
        }

        /* inlines */
        function update_inline_labels() {
            $(".inline-group").each(function() {
                $(this).find(".tabular.inline-related tbody tr:visible").each(function(i) {
                    update_inline_label($(this), i);
                });
            });
        }

        /* Password */
        $(".grp-readonly").find(":input:not(.vCheckboxInput)").attr("readonly", "readonly");
        $(".grp-readonly").find("a").on("click", function(event){
            event.preventDefault();
        });

        /* autosubmitting of filters */
        $('.grp-filter .grp-filter-content select, .grp-filter .grp-filter-content input').on('change', function(evt){
            $(this).closest('form').submit();
        });

        /* help_text_popover */
        $(':input.help-popover').popover({html: true, trigger: 'hover', placement: 'right'});

        /* formset handling */
        $('.add-row a, .grp-add-handler').on("click", function(event) {
            var id = $(this).attr("id").split("-")[0];
            var form = $("#" + id + "-empty-form");

            var template = form.html().replace(/__prefix__/g, id + "-__prefix__").replace(/empty/g, "filled");
            var count = parseInt($("#id_" + id + "-TOTAL_FORMS").val(), 10);
            $(template.replace(/__prefix__/g, count)).insertBefore($(this).closest(".inline-group").find(".tabular.inline-related tbody tr:last"));
            $("#id_" + id + "-TOTAL_FORMS").val(count + 1);
            update_inline_labels();
        });

        $('.grp-delete-handler').on("click", function(event) {
            var inline = $(this).closest(".inline-related");
            if (inline.find("tbody tr").length > 1) {
                var row = $(this).closest("tr");
                if (row.hasClass("has_original")) {
                    row.find("input:checkbox").attr("checked", true);
                    row.hide();
                } else {
                    row.remove();
                }
            }
            event.preventDefault();
            update_inline_labels();
        });

        update_inline_labels();

        /* update formsets after the admin filters were used */
        $(".grp-changelist").on("change", "select.filter", function(event) {
            $(this).closest("form").submit();
        });

    });
})(django.jQuery);
