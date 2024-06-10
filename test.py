import gradio as gr


# 定义按钮组
def create_button_group(group_name):
    num = {"Group 1": 3, "Group 2": 6, "Group 3": 9}
    # return [gr.Button(f"{group_name} 按钮 {1}")]
    return [gr.Button(f"{group_name} 按钮 {i}") for i in range(1, num[group_name]+1)]


# 定义回调函数
def show_message(button_name):
    return f"{button_name} 被点击了!"

# 定义回调函数
def show_group(group_name):
    num = {"Group 1": 3, "Group 2": 6, "Group 3": 9}
    groups = ["Group 1", "Group 2", "Group 3"]
    visibility = []
    for group in groups:
        if group == group_name:
            visibility.extend([gr.update(visible=True)] * num[group])
        else:
            visibility.extend([gr.update(visible=False)] * num[group])
    return visibility


# 创建界面
with gr.Blocks() as demo:
    with gr.Row():
        button1 = gr.Button("显示 Group 1")
        button2 = gr.Button("显示 Group 2")
        button3 = gr.Button("显示 Group 3")

    with gr.Row():
        group1_buttons = create_button_group("Group 1")
        group2_buttons = create_button_group("Group 2")
        group3_buttons = create_button_group("Group 3")

    # 默认隐藏第二组和第三组按钮
    for btn in group2_buttons + group3_buttons:
        btn.visible = False

    message_box = gr.Textbox(label="消息", interactive=False)

    # 绑定按钮点击事件显示消息
    for btn in group1_buttons + group2_buttons + group3_buttons:
        btn.click(lambda btn=btn: show_message(btn.value), None, message_box)

    # 绑定按钮点击事件
    button1.click(lambda: show_group("Group 1"), None, group1_buttons + group2_buttons + group3_buttons)
    button2.click(lambda: show_group("Group 2"), None, group1_buttons + group2_buttons + group3_buttons)
    button3.click(lambda: show_group("Group 3"), None, group1_buttons + group2_buttons + group3_buttons)

# 启动界面
demo.launch()
