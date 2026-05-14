from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, StudentResult
import pandas as pd
import os

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')


@admin_bp.route('/upload-results', methods=['GET', 'POST'])
def upload_results():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            try:
                df = pd.read_csv(file)
                for index, row in df.iterrows():
                    # Assuming CSV columns: roll_no, name, year, gpa, degree
                    student = StudentResult(
                        roll_no=row['roll_no'],
                        name=row['name'],
                        year=row['year'],
                        gpa=row['gpa'],
                        degree=row['degree']
                    )
                    db.session.add(student)
                db.session.commit()
                flash('Results imported successfully!', 'success')
            except Exception as e:
                flash(f'Error importing data: {str(e)}', 'danger')
        else:
            flash('Invalid file format. Please upload a CSV.', 'danger')

    return render_template('admin/upload.html')