# # English Prompt
# TEXT_EVAL_METRICS = {
#     "Fluency": """ Fluency: The fluency of the extracted triples '{{TGT}}'. """,
#     "Relevance": """ Relevance: The semantic consistency and relevance of the triples '{{TGT}}' with the source text '{{SRC}}'. """,
#     "Informativeness": """ Informativeness: Does the extracted triples '{{TGT}}' contain sufficient and rational information extracted from '{{SRC}}'.""",
# }
#
# TEXT_EVAL_GENERAL_PROMPT_PATTERN = """
# [Task Description]
# Here is a point-wise Knowledge Triple Extraction task. All [Input] are in English.
# The task involves extracting knowledge triples in the form of (head entity, relation, tail entity) from the given text.
# Your are required to act as a professional native-speaker human annotator to judge the extracted triples '{{TGT}}' in [Input].
# Your evaluation should follow the [Criteria] and [Guidance].
# The output format should follow the [Output Format].
#
# [Guidance]
# You should strictly follow my guidance:
# 1. Each score is between {{MIN_SCORE}} (lowest) and {{MAX_SCORE}} (highest).
# 2. Each score should be an integer score.
# 3. You should strictly follow the given output format and can't output other information.
# Do not include triples that are not supported by the text or are based on common knowledge not present in the text.
# If you break my guidance, you will be penalized.
#
# [Criteria]
# - Fluency: Evaluate how naturally the extracted triples are presented.
# - Relevance: Assess the connection and relevance of the triples to the source text.
# - Informativeness: Determine if the triples provide new and rational information based on the source text.
#
# {{In-Context Examples}}
#
# [Output Format]
# Your output should strictly follow this format and can be directly decoded by Python:
# '''
# [
#     {
#         "Fluency": {{Fluency_Score}},
#         "Relevance": {{Relevance_Score}},
#         "Informativeness": {{Informativeness_Score}},
#         "Triple": "{{Head_Entity}}, {{Relation}}, {{Tail_Entity}}"
#     },
#     ...  # More triples follow the same format
# ]
# '''
#
# [Input]
# '''
# {
#     "{{SRC}}": "The quick brown fox jumps over the lazy dog.",
#     "{{TGT}}": "fox, jumps over, dog"
# }
# '''
#
# """


# # 中文prompt
# TEXT_EVAL_METRICS = {
#     "Fluency": """ 流畅性：抽取的三元组 '{{TGT}}' 的流畅性。 """,
#     "Relevance": """ 相关性：源文本 '{{SRC}}' 与抽取的三元组 '{{TGT}}' 之间的语义一致性和相关性。 """,
#     "Informativeness": """ 信息量：抽取的三元组 '{{TGT}}' 是否包含足够的合理信息。""",
# }
#
# TEXT_EVAL_GENERAL_PROMPT_PATTERN = """
# [任务描述]
# 这是一个逐项的知识三元组抽取任务。所有的[输入]都是中文。
# 任务涉及从给定文本中抽取形式为（头实体，关系，尾实体）的知识三元组。
# 你需要作为一名专业的母语为中文的人类注释者来评价[输入]中的 '{{TGT}}'。
# 你的评价应该遵循[评价准则]和[指导原则]。
# 输出格式应该遵循[输出格式]。
#
# [指导原则]
# 你应该严格遵循我的指导原则：
# 1. 每个评分都在{{MIN_SCORE}}（最低）和{{MAX_SCORE}}（最高）之间。
# 2. 每个评分应该是整数分。
# 3. 你应该严格遵循给定的输出格式，不能输出其他信息。
# 不要包括文本中没有支持的三元组或者基于文本中不存在的常识。
# 如果你违反了我的指导原则，你将受到惩罚。
#
# [评价准则]
# - 流畅性：评估抽取的三元组呈现的自然程度。
# - 相关性：评估三元组与源文本的联系和相关性。
# - 信息量：确定三元组是否基于源文本提供新的合理信息。
#
# {{示例}}
#
# [输出格式]
# 你的输出应该严格遵循这个格式，并且能够被Python直接解码：
# '''
# [
#     {
#         "流畅性": {{流畅性评分}},
#         "相关性": {{相关性评分}},
#         "信息量": {{信息量评分}},
#         "三元组": "{{头实体}}, {{关系}}, {{尾实体}}"
#     },
#     ...  # 更多三元组遵循相同的格式
# ]
# '''
#
# [输入]
# '''
# {
#     "{{SRC}}": "快速的棕色狐狸跳过了懒狗。",
#     "{{TGT}}": "狐狸, 跳过, 狗"
# }
# '''
#
# """


TEXT_EVAL_METRICS = {
    "Fluency": """ Fluency: The fluency of the '{{TGT}}'. """,
    "Relevance": """ Relevance: The semantic consistency and relevance between '{{SRC}}' and '{{TGT}}'. """,
    "Informativeness": """ Informativeness: Does '{{TGT}}' contain sufficient and rational information.""",
}

TEXT_EVAL_GENERAL_PROMPT_PATTERN = """
[Task Description]
Here is a point-wise {{TASK_NAME}} task. All [Input] are in {{Language}}.
{{MORE_TASK_DEFINITION}}
Your are required to acted as a professional native-speaker human annotator to judge the given {{TGT}} in [Input].
Your evaluation should follow the [Criteria] and  [Guidance].
The output format should follow the [Output Format].

[Guidance]
You should strictly follow my guidance:
1. Each score is between {{MIN_SCORE}} (lowest) and {{MAX_SCORE}} (highest).
2. Each score should be {{DATATYPE}} score.
3. You should strictly follow the given output format and can't output other information.
{{MORE_GUIDANCE}}
If you break my guidance, you will be penalized.

[Criteria]
{{Criteria}}

{{In-Context Examples}}

[Output Format]
Your output should strictly follow this format and can be directly decoded by Python:
'''
{{Output}}
'''

[Input]
'''
{
    "{{SRC}}": {{SRC_VALUE}},
    "{{TGT}}": {{TGT_VALUE}}
}
'''

"""
