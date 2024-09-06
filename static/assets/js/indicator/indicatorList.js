$(document).ready(function () {

    let rowCounter = 0

    const table = (data) => {
        let parentLists = data.indicators.filter((item) => item.parent_id == null)
        let childLists = (parentId, space) => {
            let childList = data.indicators.filter((item) => item.parent_id == parentId)
            return childList.map((item) => {
                return `
                <tr>
                   <td>${rowCounter + 1}</td>    
                   <td>${space} ${item.title_AMH}</td>
                   <td>${space} ${item.title_ENG}</td>
                   <td>${space} ${item.composite_key}</td>
                   <td></td>
                   <td>${item.measurement_units ? item.measurement_units : " - "}</td>
                   <td>${item.kpi_characteristics ? item.kpi_characteristics : " - "}</td>
                   <td>${item.is_dashboard_visible ? ` <i class="fa fa-check text-success"></i>` : `<i class="fa fa-times text-danger"></i>`}</td>
                   <td>${item.is_public ? ` <i class="fa fa-check text-success"></i>` : `<i class="fa fa-times text-danger"></i>`}</td>
                   <td> <a href="/user-admin/indicator_details/${item.id}"><i class="fa fa-eye text-info"></i> </a> </td>
                </tr>
                ${space += String("&nbsp;&nbsp;&nbsp;&nbsp")}
                ${rowCounter++}
                ${childLists(item.id, space)}
                `
            })
        }

        let tableRow = ''
        if (parentLists.length == 0) {
            tableRow = `<tr class="text-bold text-center text-danger" ><td colspan="10">No data found</td></tr>`
        } else {
            tableRow = parentLists.map((item) => {
                return `
                <tr class="text-bold">
                   <td>${rowCounter + 1}</td>    
                   <td>${item.title_AMH}</td>
                   <td>${item.title_ENG}</td>
                   <td>${item.composite_key}</td>
                   <td> ${item.for_category ? item.for_category.slice(0, 2).join(", ") + "..." : " - "} </td>
                   <td>${item.measurement_units ? item.measurement_units : " - "}</td>
                   <td>${item.kpi_characteristics ? item.kpi_characteristics : " - "}</td>
                   <td>${item.is_dashboard_visible ? ` <i class="fa fa-check text-success"></i>` : `<i class="fa fa-times text-danger"></i>`}</td>
                   <td>${item.is_public ? ` <i class="fa fa-check text-success"></i>` : `<i class="fa fa-times text-danger"></i>`}</td>
                   <td> <a href="/user-admin/indicator_details/${item.id}"><i class="fa fa-eye text-info"></i> </a> </td>
                </tr>
                ${rowCounter++}
                ${childLists(item.id, "&nbsp;&nbsp;&nbsp;&nbsp").join("")}
                `
            })
        }

        $("#renderTable").html(tableRow)
    }

    const fetchTableData = async () => {
        let urlPath = window.location.pathname;
        let pathID = urlPath.replace("/user-admin/indicators/", "");
        let response = await useFetch(`http://127.0.0.1:8000/indicator-lists/${pathID}`)

        //Hide for category 
        $("#id_for_category").parent().hide()
        //select default category
        $("#id_for_category").val(pathID)


        table(response)


    }

    fetchTableData()


})