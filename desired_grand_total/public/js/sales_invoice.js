frappe.ui.form.on('Sales Invoice', {
    desired_grand_total: function (frm) {
		// Fetch the conversion rate and the invoice currency
		let conversion_rate = frm.doc.conversion_rate || 1; // Default to 1 if no conversion rate is set
		let currency = frm.doc.currency || frappe.sys_defaults.currency; // Use default currency if not set

		// Fetch tax rate from the taxes table or set to 0 if no taxes
		let tax_rate = 0;
		if (frm.doc.taxes && frm.doc.taxes.length > 0) {
			frm.doc.taxes.forEach(tax => {
				if (tax.rate) {
					tax_rate += tax.rate / 100;
				}
			});
		}

		// Handle cases where tax_rate is zero
		if (tax_rate === 0) {
			frappe.msgprint(__('No taxes are applied or tax rate is zero. Calculation will proceed without taxes.'));
		}

		// Ensure there's a valid desired_grand_total
		if (frm.doc.desired_grand_total) {
			// Calculate the new net total in the base currency
			let new_net_total_base = tax_rate > 0 
				? frm.doc.desired_grand_total / (1 + tax_rate) 
				: frm.doc.desired_grand_total;

			// Convert the net total to the base currency
			let new_net_total = new_net_total_base / conversion_rate;

			// Calculate the original net total in the base currency
			let original_net_total_base = frm.doc.net_total; // Total before tax
			if (!original_net_total_base || original_net_total_base === 0) {
				frappe.msgprint(__('Please ensure the items total is set.'));
				return;
			}

			// Calculate the reduction percentage
			let reduction_percent = ((original_net_total_base - new_net_total) / original_net_total_base) * 100;

			// Update the reduction_percent field
			frm.set_value('reduction_percent', reduction_percent.toFixed(2));

			// Prompt for confirmation before proceeding
			frappe.confirm(
				__('The reduction percent is calculated as {0}%. Do you want to adjust item rates accordingly?', [reduction_percent.toFixed(2)]),
				function () {
					// If user confirms, adjust item prices proportionally
					frm.doc.items.forEach(item => {
						let original_rate = item.rate; // Original item rate in the invoice currency
						let new_rate = original_rate * (1 - reduction_percent / 100);
						frappe.model.set_value(item.doctype, item.name, 'rate', new_rate.toFixed(2));
					});

					frm.refresh_field('items');
					frappe.msgprint(__('Item rates have been updated successfully.'));
				},
				function () {
					// If user cancels, do nothing
					frappe.msgprint(__('No changes were made to item rates.'));
				}
			);
		}
	}
});
