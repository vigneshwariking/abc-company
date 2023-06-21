from odoo import models, fields, api


class ReportMember(models.Model):
    _name = 'report.abc.report_member_template'
    _description = 'Report member'

    @api.model
    def _get_report_values(self, docids, data=None):
        member_ids = data['member_ids']
        docs = self.env['member.member'].browse(member_ids)
        docs = self.env['member.member'].search(
            ['|', ('id', 'in', member_ids),
             ('start_date', '>=', data['start_date']),
             ('end_date', '<=', data['end_date'])])

        print('>>>>>>>>>>>>>>>>>>>>>', docs)

        return {
            'doc_ids': docids,
            'doc_model': 'member.member',
            'docs': docs,
        }