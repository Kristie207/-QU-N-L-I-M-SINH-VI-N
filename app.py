
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Tiêu đề ứng dụng
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Dữ liệu sinh viên
data = {
    "Họ tên": [
        "Nguyễn Bảo", "Trần Bình", "Lê Chi", "Phạm Dũng",
        "Hoàng Anh", "Võ Giang", "Phan Huy", "Bùi Lan",
        "Ngô Minh", "Đỗ Nam"
    ],
    "Chuyên cần": [9, 8, 10, 7, 9, 8, 6, 10, 9, 7],
    "Giữa kỳ": [8, 7, 9, 6, 8, 7, 5, 9, 8, 6],
    "Cuối kỳ": [8.5, 7.5, 9.5, 6.5, 8, 7, 5.5, 9, 8.5, 7]
}

df = pd.DataFrame(data)

# Tính điểm tổng kết
df["Tổng kết"] = (
    df["Chuyên cần"] * 0.2
    + df["Giữa kỳ"] * 0.3
    + df["Cuối kỳ"] * 0.5
).round(2)

# Xếp loại
df["Xếp loại"] = "Yếu"
df.loc[df["Tổng kết"] >= 5, "Xếp loại"] = "Trung bình"
df.loc[df["Tổng kết"] >= 7, "Xếp loại"] = "Khá"
df.loc[df["Tổng kết"] >= 8.5, "Xếp loại"] = "Giỏi"

# Hiển thị bảng điểm
st.subheader("Bảng điểm sinh viên")
st.dataframe(df, hide_index=True, use_container_width=True)

# Thống kê
st.subheader("Thống kê")

st.write("Điểm trung bình của lớp:", round(df["Tổng kết"].mean(), 2))

cao = df["Tổng kết"].max()
thap = df["Tổng kết"].min()

st.write("Sinh viên có điểm cao nhất:")
st.write(df[df["Tổng kết"] == cao][["Họ tên", "Tổng kết"]])

st.write("Sinh viên có điểm thấp nhất:")
st.write(df[df["Tổng kết"] == thap][["Họ tên", "Tổng kết"]])

st.write("Số sinh viên đạt:", (df["Tổng kết"] >= 5).sum())

# Chọn sinh viên
st.subheader("Tra cứu điểm sinh viên")

ten = st.selectbox("Chọn sinh viên:", df["Họ tên"])

sv = df[df["Họ tên"] == ten].iloc[0]

st.write("Họ tên:", sv["Họ tên"])
st.write("Điểm chuyên cần:", sv["Chuyên cần"])
st.write("Điểm giữa kỳ:", sv["Giữa kỳ"])
st.write("Điểm cuối kỳ:", sv["Cuối kỳ"])
st.write("Điểm tổng kết:", sv["Tổng kết"])
st.write("Xếp loại:", sv["Xếp loại"])

# Biểu đồ cột ngang
st.subheader("Biểu đồ điểm tổng kết")

fig, ax = plt.subplots()
ax.barh(df["Họ tên"], df["Tổng kết"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Họ tên")
ax.set_xlim(0, 10)
ax.set_xticks(range(0, 11, 2))
fig.tight_layout()

st.pyplot(fig)

# Thông tin người tạo
st.markdown("---")
st.caption("Người tạo: Nguyễn Vân Bảo Khánh | MSSV: 031308011228")
