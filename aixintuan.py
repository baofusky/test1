import streamlit as st


def display_inspirational_text():
    inspirational_text = """
    # 始终保持希望

    当生活变得艰难时,请记住:

    - 你是一个战胜困难的勇者
    - 你有能力克服任何挑战
    - 即使在最黑暗的时候,光明也终将到来
    - 相信自己,你一定能重拾希望和勇气

    生命充满无限可能,让我们一起迎接美好的未来吧。
    """
    st.markdown(inspirational_text)


if __name__ == '__main__':
    st.set_page_config(page_title="Inspirational Text")
    st.title("TO 我的老婆张春华")
    display_inspirational_text()