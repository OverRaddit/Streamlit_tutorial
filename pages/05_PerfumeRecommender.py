import streamlit as st
# from openai import OpenAI
import openai

# perfume Data
perfumeData = [
  {
    "brand_name": '바이레도',
    "name": '블랑쉬EDP',
    "perfume_code": 'C033',
    "keywords": '깔끔한,자상한,청순한',
    "color": '파랑',
    "accords": '알데히드,비누,플로럴',
    "perfume_gender": '남녀공용',
    "color_code": '#A5C7E7',
    "desc": '막 세탁을 마친 새하얀 이불에서 느껴지는 향',
  },
  {
    "brand_name": '샤넬',
    "name": '가브리엘에쌍스EDP',
    "perfume_code": 'C105',
    "keywords": '럭셔리한,,러블리한',
    "color": '노랑',
    "accords": '화이트 플로럴,시트러스,프루티',
    "perfume_gender": '여성',
    "color_code": '#FFBC3A',
    "desc": '가브리엘 샤넬을 닮아 생기 넘치면서도 따뜻한 꽃향기',
  },
  {
    "brand_name": '조 말론',
    "name": '피오니&블러쉬스웨이드Cologne',
    "perfume_code": 'C054',
    "keywords": '러블리한,,청순한',
    "color": '분홍',
    "accords": '플로럴,프루티,파우더리',
    "perfume_gender": '여성',
    "color_code": '#FBB6C1',
    "desc": '백화점 1층에 온 것 같은 향기',
  },
  {
    "brand_name": '조 말론',
    "name": '잉글리쉬페어&프리지아Cologne',
    "perfume_code": 'C051',
    "keywords": '발랄한,청량한,러블리한',
    "color": '초록',
    "accords": '프루티,플로럴,프레쉬',
    "perfume_gender": '여성,남녀공용',
    "color_code": '#ACD92E',
    "desc": '향긋하고 싱그러운 프리지아 향기',
  },
  {
    "brand_name": '프레데릭 말',
    "name": '포트레이트오브어레이디EDP',
    "perfume_code": 'C066',
    "keywords": '섹시한,클래식한,커리어우먼',
    "color": '빨강',
    "accords": '오리엔탈,장미,우디',
    "perfume_gender": '여성,남녀공용',
    "color_code": '#A41111',
    "desc": '사원 곳곳에서 풍겨오는 진한 장미 향기',
  },
  {
    "brand_name": '샤넬',
    "name": '알뤼르옴므스포츠EDT',
    "perfume_code": 'C124',
    "keywords": '스포티한,프로페셔널한,',
    "color": '파랑',
    "accords": '시트러스,남자스킨,마린',
    "perfume_gender": '남성',
    "color_code": '#64B6C8',
    "desc": '서핑보드를 들고 지나가는 서퍼에서 느껴지는 향기',
  },
  {
    "brand_name": '딥티크',
    "name": '탐다오EDP',
    "perfume_code": 'C007',
    "keywords": '자상한,클래식한,힙한,럭셔리한',
    "color": '갈색',
    "accords": '우디,오리엔탈,바닐라',
    "perfume_gender": '남성,남녀공용',
    "color_code": '#C69036',
    "desc": '높은 산자락에 자리 잡은 고즈넉한 사찰의 인센스 향',
  },
  {
    "brand_name": '르 라보',
    "name": '떼마차26EDP',
    "perfume_code": 'C139',
    "keywords": '차분한,깔끔한,깔끔한',
    "color": '초록',
    "accords": '프루티,우디,파우더리',
    "perfume_gender": '남녀공용',
    "color_code": '#A0C878',
    "desc": '유서 깊은 료칸에서 마시는 말차와 달콤한 디저트 향기',
  },
  {
    "brand_name": '메종 프란시스 커정',
    "name": '아쿠아셀레스티아포르테EDP',
    "perfume_code": 'C025',
    "keywords": '청량한,스포티한,깔끔한',
    "color": '파랑',
    "accords": '시트러스,알데히드,프레쉬',
    "perfume_gender": '남녀공용',
    "color_code": '#96F5F1',
    "desc": '에메랄드빛 바다에서 차가운 모히토 한 잔',
  },
  {
    "brand_name": '딥티크',
    "name": '오프레지아EDT',
    "perfume_code": 'C152',
    "keywords": '청순한,,러블리한,발랄한',
    "color": '초록',
    "accords": '화이트 플로럴,워터리,파우더리',
    "perfume_gender": '여성',
    "color_code": '#E9FFCE',
    "desc": '햇살 가득한 정원에서 물에 젖은 풍성한 프리지아 향기',
  },
  {
    "brand_name": '킬리안',
    "name": '굿걸곤배드EDP',
    "perfume_code": 'C085',
    "keywords": '커리어우먼,힙한,섹시한,럭셔리한',
    "color": '분홍',
    "accords": '스모키,프루티,가죽',
    "perfume_gender": '여성',
    "color_code": '#FFA2CB',
    "desc": '담배 연기 뒤에 가려진 달달한 복숭아 향기',
  },
  {
    "brand_name": '펜할리곤스',
    "name": '로드조지EDP',
    "perfume_code": 'C101',
    "keywords": '클래식한,프로페셔널한,힙한,섹시한',
    "color": '갈색',
    "accords": '위스키,스모키,바닐라',
    "perfume_gender": '남성',
    "color_code": '#703636',
    "desc": '고택 난롯가에 앉아 있는 영국 신사처럼 중후한 향',
  },
  {
    "brand_name": '샤넬',
    "name": '블루드샤넬EDP',
    "perfume_code": 'C043',
    "keywords": '프로페셔널한,클래식한,,',
    "color": '파랑',
    "accords": '남자스킨,시트러스,아로마틱',
    "perfume_gender": '남성',
    "color_code": '#3A4CA8',
    "desc": '출근길에 한 번은 맡아봤을 법한 남자 스킨 향',
  },
  {
    "brand_name": '르 라보',
    "name": '어나더13EDP',
    "perfume_code": 'C021',
    "keywords": '힙한,깔끔한,커리어우먼,차분한',
    "color": '무채색',
    "accords": '머스크,메탈릭,애니멀릭',
    "perfume_gender": '남녀공용',
    "color_code": '#D2C7BD',
    "desc": '어나더에게 선택받은 사람만 쓸 수 있는 머스크 향수',
  },
]

# Title and introduction
st.title("AI 향수추천 시뮬레이터")

# Input for the OpenAI API key
api_key = st.text_input("OpenAI API Key를 입력하세요.", type="password")
# Input for the image URL
image_url = st.text_input("이미지URL을 입력하세요.")

# Divider
st.markdown("---")

# Section for appearance description
st.subheader("🧑‍🎨 외모 묘사")
appearance_prompt = st.text_area("프로필 사진을 어떻게 묘사할지 알려주세요 :", "사진 속 인물을 보고, 그 인물과 관련된 정보를 예측하여 제시한다. 그 인물의 성별, 연령, 직업, 성격, 현재 장소, 기분 등을 추정한다.", height=150)
submit_appearance = st.button("Submit Appearance Description")

# Initialize response area for appearance
if 'response_appearance' not in st.session_state:
  st.session_state.response_appearance = ""

# Validate API key presence for appearance submission
if submit_appearance:
  if not api_key:
    st.error("API Key가 필요합니다.")
  else:
    # OpenAI API call
    try:
      openai.api_key = api_key
      response = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
          {
            "role": "user",
            "content": [
              {"type": "text", "text": f"{appearance_prompt}"},
              {
                "type": "image_url",
                "image_url": {
                  "url": image_url,
                },
              },
            ],
          },
        ],
        max_tokens=1000
      )
      # why?????????????????
      # this work. response.choices[0].message.content
      # this isn't work. response.choices[0].message['content']

      st.session_state.response_appearance = response.choices[0].message.content
    except Exception as e:
      st.error(f"API 호출 중 오류가 발생했습니다: {str(e)}")

# Display the response in a text_area widget using the value from session_state
response_area = st.text_area("답변:", value=st.session_state.response_appearance, height=150)

st.markdown("---")

# Section for perfume recommendation
st.subheader("👨‍🏫 향수 추천")
perfume_prompt = st.text_area("chatGPT에게 향수가 추천될 방법을 설명해주세요 :",
                              f"""한국어로 대답하세요.
당신은 10년 경력의 데이터 전문가입니다. 당신은 주어진 정보를 종합하여 향수를 추천해야 합니다.

조합 방법은 다음과 같습니다.
1. 내가 제시한 3개의 가장 관련성이 높은 키워드를 인물의 외관 묘사 정보에서 추출한다
2. 제시된 향수 데이터와 일치시켜 증거가 있는 향수 추천

키워드 목록은 다음과 같습니다.
깔끔한
럭셔리한
러블리한
발랄한
섹시한
스포티한
자상한
차분한
청량한
청순한
커리어우먼
클래식한
프로페셔널한
힙한

# 당신이 추천할 수 있는 후보의 향수 데이터
[[{perfumeData}]]

# 당신의 고객에 대한 정보
[[{st.session_state.response_appearance}]]

당신의 고객이 선호할만한 향수를 추천하고, 왜 그 향수를 추천했는지에 대해 재미있게 풀어서 설명하세요.
"""
                              ,height=150)
submit_perfume = st.button("Submit Perfume Recommendation")
st.session_state.perfume_response = st.empty()  # Use st.empty to create a placeholder for dynamic content

if 'response_perfume' not in st.session_state:
  st.session_state.response_perfume = ""

# Validate both API key presence and non-empty appearance response for perfume submission
if submit_perfume:
  if not api_key:
    st.error("API Key가 필요합니다.")
  elif st.session_state.response_appearance == "":
    st.error("외모 묘사에 대한 응답을 먼저 받아야 합니다.")
  else:
    # OpenAI API call
    try:
      openai.api_key = api_key
      response = openai.chat.completions.create(
        # model="gpt-4-turbo",
        model="gpt-3.5-turbo",
        messages=[
          {
            "role": "user",
            "content": [
              {"type": "text", "text": f"{perfume_prompt}"},
            ],
          },
        ],
        max_tokens=1000
      )

      st.session_state.response_perfume = response.choices[0].message.content
    except Exception as e:
      st.error(f"API 호출 중 오류가 발생했습니다: {str(e)}")

# Output area for perfume recommendation response
perfume_response_area = st.text_area("답변:", value=st.session_state.response_perfume, height=150, key="response_perfume")

# 파일 내용
file_content = f"""

이미지 URL:

{image_url}

----

외모 묘사 프롬프트:

{appearance_prompt}

----

외모 묘사 답변:

{st.session_state.response_appearance}

----

향수 추천 프롬프트:

{perfume_prompt}

----

향수 추천 답변:

{st.session_state.response_perfume}

----
"""

st.markdown("---")

# 다운로드 버튼
st.download_button(label="Download Text File",
                   data=file_content,
                   file_name="perfume_recommendation.txt",
                   mime="text/plain")
