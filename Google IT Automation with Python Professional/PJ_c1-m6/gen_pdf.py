def provide_pdf(current_users, filename='report.pdf'):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, height - 80, "Server Name")
    c.drawString(300, height - 80, "Logged In User")

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, "Current logged in user Report")

    c.setFont("Helvetica", 12)
    y_position = height - 100  # 初期Y位置

    for machine, users in current_users.items():
        if users:  # ユーザーがいる場合のみ出力
            user_list = ", ".join(users)
            c.drawString(100, y_position, f"{machine}: {user_list}")
            y_position -= 20  # 次の行のY位置を下げる

            # ページの下部に達した場合、新しいページを作成
            if y_position < 50:
                c.showPage()
                c.setFont("Helvetica", 12)
                c.drawString(100, height - 80, "Server Name")
                c.drawString(300, height - 80, "Logged In User")
                y_position = height - 100  # Y位置をリセット

    c.save()
