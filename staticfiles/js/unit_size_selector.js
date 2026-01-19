document.addEventListener("DOMContentLoaded", function () {
    const unitSelect = document.getElementById("unit_id");
    const unitSizeSelect = document.getElementById("unit_size");
    const qtyInput = document.getElementById("quantity");
    const pointsPreview = document.getElementById("points_per_unit_preview");
    const subtotalPreview = document.getElementById("subtotal_preview");

    function updatePreviews(data) {
        if (!pointsPreview || !subtotalPreview) return;
        if (!data) {
            pointsPreview.textContent = "";
            subtotalPreview.textContent = "";
            return;
        }
        const size = parseInt(unitSizeSelect.value || data.min_size, 10);
        const scaled = Math.floor((data.points * size) / data.min_size);
        pointsPreview.textContent = `${scaled} pts`;
        const qty = parseInt(qtyInput?.value || "1", 10);
        subtotalPreview.textContent = `${scaled * qty} pts`;
    }

    async function fetchUnitData(unitId) {
        try {
            const response = await fetch(`/core/api/unit/${unitId}/`);
            const data = await response.json();
            return response.ok ? data : null;
        } catch (err) {
            console.error("Error fetching unit details:", err);
            return null;
        }
    }

    unitSelect?.addEventListener("change", async function () {
        const unitId = this.value;
        if (!unitId) {
            unitSizeSelect.innerHTML =
                '<option value="">Select a unit size...</option>';
            updatePreviews(null);
            return;
        }

        const data = await fetchUnitData(unitId);
        if (!data) {
            updatePreviews(null);
            return;
        }

        // Populate unit size options
        unitSizeSelect.innerHTML = "";
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
        unitSizeSelect.value = data.min_size;

        // Initial preview and listeners
        updatePreviews(data);
        unitSizeSelect.onchange = () => updatePreviews(data);
        qtyInput?.addEventListener("input", () => updatePreviews(data));
    });
});
