import io
from datetime import datetime
import mimetypes
# import

from flask import render_template, Response, send_file
from flask_login import login_required

import xlsxwriter

from app import db
from . import bp


# @bp.route('/')
@bp.route('/reports')
@login_required
def index():
    # user = User.query.filter_by(username='natalya').first_or_404()
    # posts = [
    #     {
    #         'author': User.query.filter_by(username='natalya').first(),
    #         'body': 'Beautiful day in Portland!'
    #     },
    #     {
    #         'author': User.query.filter_by(username='susan').first(),
    #         'body': 'The Avengers movie was so cool!'
    #     }
    # ]
    return render_template('reports/index.html', title='Reports', )


def get_simple_table_data():
    # Simulate a more complex table read.
    return [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]


@bp.route('/reports/download')
def get_xslx_for_data():
    # Create an in-memory output file for the new workbook.
    output = io.BytesIO()

    # Even though the final file will be in memory the module uses temp
    # files during assembly for efficiency. To avoid this on servers that
    # don't allow temp files, for example the Google APP Engine, set the
    # 'in_memory' Workbook() constructor option as shown in the docs.
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    # Get some data to write to the spreadsheet.
    data = get_simple_table_data()

    # Write some test data.
    for row_num, columns in enumerate(data):
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num, col_num, cell_data)

    # Close the workbook before sending the data.
    workbook.close()

    # Rewind the buffer.
    output.seek(0)

    # Set up the Http response.
    filename = 'django_simple.xlsx'
    response = Response(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',

    )
    response.headers['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response