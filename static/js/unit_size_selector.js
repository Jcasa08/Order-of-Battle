document
    .getElementById("unit_id")
    .addEventListener("change", async function () {
        const unitId = this.value;
        if (!unitId) {
            // Reset to defaults if no unit selected
            document.getElementById("unit_size").value = "5";
            document.getElementById("unit_size").min = "1";
            document.getElementById("unit_size").max = "";
            document.getElementById("unit_size").step = "1";
            return;
        }

        try {
            const response = await fetch(`/core/api/unit/${unitId}/`);
            const data = await response.json();

            if (response.ok) {
                // Update unit_size input with unit's min_size, max_size, and step
                document.getElementById("unit_size").value = data.min_size;
                document.getElementById("unit_size").min = data.min_size;
                document.getElementById("unit_size").max = data.max_size;
                document.getElementById("unit_size").step = data.min_size;
            } else {
                console.error("Error fetching unit details:", data.error);
            }
        } catch (error) {
            console.error("Error:", error);
        }
    });
