document
            .getElementById("unit_id")
            .addEventListener("change", async function () {
                const unitId = this.value;
                const unitSizeSelect = document.getElementById("unit_size");

                if (!unitId) {
                    // Reset to defaults if no unit selected
                    unitSizeSelect.innerHTML =
                        '<option value="">Select a unit size...</option>';
                    return;
                }

                try {
                    const response = await fetch(`/core/api/unit/${unitId}/`);
                    const data = await response.json();

                    if (response.ok) {
                        // Clear existing options
                        unitSizeSelect.innerHTML = "";

                        // Generate options from min_size to max_size, incrementing by min_size
                        for (
                            let size = data.min_size;
                            size <= data.max_size;
                            size += data.min_size
                        ) {
                            const option = document.createElement("option");
                            option.value = size;
                            option.textContent = size;
                            unitSizeSelect.appendChild(option);
                        }

                        // Select the first (minimum) option by default
                        unitSizeSelect.value = data.min_size;
                    } else {
                        console.error(
                            "Error fetching unit details:",
                            data.error
                        );
                    }
                } catch (error) {
                    console.error("Error:", error);
                }
            });
