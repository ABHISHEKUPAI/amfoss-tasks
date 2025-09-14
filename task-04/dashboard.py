import sys
import csv
import mysql.connector
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QTableWidget, QTableWidgetItem, QGridLayout,
    QTextEdit, QSizePolicy, QLineEdit, QFileDialog
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CineScope – Dashboard")
        self.setMinimumSize(1200, 800)
        self.setStyleSheet("background-color: #121212; color: white; padding: 20px;")
        self.init_ui()

        # --- Connect to MySQL ---
        self.db_conn = mysql.connector.connect(
            host="localhost",
            user="abhishek",
            password="krishna123",
            database="cinescope_db"
        )
        self.db_cursor = self.db_conn.cursor(dictionary=True)

        # --- Track state ---
        self.search_mode = None
        self.selected_columns = []

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        # Header
        header = QLabel("🎬 CineScope Dashboard")
        header.setFont(QFont("Arial", 24, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        header.setFixedHeight(80)
        main_layout.addWidget(header)

        split_layout = QHBoxLayout()

        # Left Panel
        left_container = QVBoxLayout()
        left_container.setSpacing(10)
        left_container.setAlignment(Qt.AlignTop)

        # Search buttons
        search_heading = QLabel("Search By")
        search_heading.setFont(QFont("Arial", 18, QFont.Bold))
        left_container.addWidget(search_heading)

        search_buttons = [
            ("Genre", "genre"),
            ("Year", "year"),
            ("Rating", "rating"),
            ("Director", "director"),
            ("Actor", "actor"),
        ]

        search_grid = QGridLayout()
        for index, (label, mode) in enumerate(search_buttons):
            btn = QPushButton(label)
            btn.setStyleSheet(self.get_button_style(False))
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            btn.clicked.connect(lambda _, m=mode: self.set_search_mode(m))
            row, col = divmod(index, 2)
            search_grid.addWidget(btn, row, col)
        left_container.addLayout(search_grid)

        # Column selection
        column_heading = QLabel("Select Columns")
        column_heading.setFont(QFont("Arial", 18, QFont.Bold))
        left_container.addWidget(column_heading)

        column_buttons = [
            ("Title", "title"),
            ("Year", "year"),
            ("Genre", "genre"),
            ("Rating", "rating"),
            ("Director", "director"),
            ("Stars", "star1, star2, star3"),
        ]

        column_grid = QGridLayout()
        for index, (label, col) in enumerate(column_buttons):
            btn = QPushButton(label)
            btn.setStyleSheet(self.get_button_style(False))
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            btn.clicked.connect(lambda _, c=col: self.toggle_column(c))
            row, colpos = divmod(index, 2)
            column_grid.addWidget(btn, row, colpos)
        left_container.addLayout(column_grid)

        # Search input
        self.query_input = QLineEdit()
        self.query_input.setPlaceholderText("Enter search term")
        self.query_input.setStyleSheet(
            "background-color: #1e1e1e; color: white; padding: 5px; border: 1px solid #444;"
        )
        left_container.addWidget(self.query_input)

        # Action buttons
        action_layout = QHBoxLayout()
        search_btn = QPushButton("Search")
        search_btn.setStyleSheet(
            "background-color: #e50914; color: white; padding: 6px; border-radius: 5px;"
        )
        search_btn.clicked.connect(self.execute_search)
        action_layout.addWidget(search_btn)

        export_btn = QPushButton("Export CSV")
        export_btn.setStyleSheet(
            "background-color: #1f1f1f; color: white; padding: 6px; border-radius: 5px;"
        )
        export_btn.clicked.connect(self.export_csv)
        action_layout.addWidget(export_btn)
        left_container.addLayout(action_layout)

        # Right Panel
        right_side_layout = QVBoxLayout()
        right_side_layout.setSpacing(10)

        # Table
        self.table = QTableWidget()
        self.table.setStyleSheet("""
            QTableWidget {
                color: white;
                font-family: Arial, sans-serif;
                font-size: 14px;
            }
            QHeaderView::section {
                background-color: white;
                color: black;
                padding: 4px;
            }
        """)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Output console
        self.output_console = QTextEdit()
        self.output_console.setPlaceholderText("Results will appear here...")
        self.output_console.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: white;
                border: 1px solid #444;
                padding: 5px;
            }
        """)
        self.output_console.setFixedHeight(100)

        right_side_layout.addWidget(self.table)
        right_side_layout.addWidget(self.output_console)

        split_layout.addLayout(left_container, 2)
        split_layout.addLayout(right_side_layout, 8)
        main_layout.addLayout(split_layout)
        self.setLayout(main_layout)

    # === Logic methods ===
    def get_button_style(self, is_selected):
        if is_selected:
            return """
                QPushButton {
                    background-color: #ffcc00;
                    border: 1px solid #ff9900;
                    border-radius: 3px;
                    padding: 6px;
                }
            """
        else:
            return """
                QPushButton {
                    background-color: #1f1f1f;
                    border: 1px solid #333;
                    border-radius: 3px;
                    padding: 6px;
                }
                QPushButton:hover {
                    background-color: #333;
                }
            """

    def set_search_mode(self, mode):
        self.search_mode = mode
        self.output_console.append(f"🔍 Search mode set to: {mode}")

    def toggle_column(self, column):
        if column in self.selected_columns:
            self.selected_columns.remove(column)
            self.output_console.append(f"❌ Column removed: {column}")
        else:
            self.selected_columns.append(column)
            self.output_console.append(f"✅ Column added: {column}")

    def execute_search(self):
        query_text = self.query_input.text().strip()
        if not self.search_mode or not query_text:
            self.output_console.append("⚠️ Please select a search mode and enter text.")
            return

        # columns
        if self.selected_columns:
            columns = ", ".join(self.selected_columns)
        else:
            columns = "*"

        # build query
        if self.search_mode == "actor":
            sql = f"""
                SELECT {columns} FROM movies
                WHERE star1 LIKE %s OR star2 LIKE %s OR star3 LIKE %s
            """
            params = (f"%{query_text}%", f"%{query_text}%", f"%{query_text}%")
        else:
            sql = f"SELECT {columns} FROM movies WHERE {self.search_mode} LIKE %s"
            params = (f"%{query_text}%",)

        self.db_cursor.execute(sql, params)
        rows = self.db_cursor.fetchall()

        if not rows:
            self.table.setRowCount(0)
            self.table.setColumnCount(0)
            self.output_console.append("No results found.")
            return

        headers = list(rows[0].keys())
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setRowCount(len(rows))

        for r, row in enumerate(rows):
            for c, h in enumerate(headers):
                item = QTableWidgetItem(str(row[h]) if row[h] is not None else "")
                self.table.setItem(r, c, item)

        self.output_console.append(f"✅ Found {len(rows)} results.")

    def export_csv(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save CSV", "results.csv", "CSV Files (*.csv)")
        if not path:
            return

        row_count = self.table.rowCount()
        col_count = self.table.columnCount()
        headers = [self.table.horizontalHeaderItem(i).text() for i in range(col_count)]

        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            for r in range(row_count):
                row = []
                for c in range(col_count):
                    item = self.table.item(r, c)
                    row.append(item.text() if item else "")
                writer.writerow(row)

        self.output_console.append(f"💾 Exported {row_count} rows to {path}")

    def closeEvent(self, event):
        try:
            self.db_cursor.close()
            self.db_conn.close()
        except:
            pass
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec())
