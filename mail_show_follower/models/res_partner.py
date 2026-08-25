from odoo import models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def _filter_shown_in_cc(self, show_internal_users):
        """Get partners that should be displayed as CC on mails."""
        # Never display hidden users
        result = self.filtered_domain(
            [
                "|",
                ("user_ids", "=", False),
                ("user_ids.show_in_cc", "=", True),
            ]
        )
        # Remove internal users from result if needed
        if not show_internal_users:
            internal_users = result.filtered_domain(
                [
                    ("user_ids.active", "=", True),
                    # Odoo 19: "groups_id" was renamed and now only holds
                    # explicitly assigned groups. Use "all_group_ids" (incl.
                    # implied groups) to match the pre-19 "groups_id" behavior
                    # -- this is also how odoo core's own _compute_share does
                    # the internal-user check.
                    (
                        "user_ids.all_group_ids",
                        "in",
                        self.env.ref("base.group_user").ids,
                    ),
                ]
            )
            result -= internal_users
        return result
