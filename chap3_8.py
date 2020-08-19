# import requests
# from bs4 import BeautifulSoup
# #引入request和bs
#
# url='https://www.zhihu.com/people/lisanshui1230/posts?page=1'
# headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
# #使用headers
# res=requests.get(url,headers=headers)
# #发起请求，将响应的结果赋值给变量res。
# print(res.status_code)
# #检查状态码
# bstitle=BeautifulSoup(res.text,'html.parser')
# #用bs进行解析
# title=bstitle.findAll(class_='ContentItem-title')
# #提取我们想要的标签和里面的内容
# print(title)
# #打印title




# import requests
# from bs4 import BeautifulSoup
# #引入request和bs
#
# url='https://www.zhihu.com/people/lisanshui1230/posts?page=1'
# headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
# #使用headers
# res=requests.get(url,headers=headers)
# #发起请求，将响应的结果赋值给变量res。
# print(res.status_code)
# #检查状态码
# bstitle=BeautifulSoup(res.text,'html.parser')
# #用bs进行解析
# title=bstitle.findAll(class_='ContentItem-title')
# #提取我们想要的标签和里面的内容
# print(title)
# #打印title
# print(res.text)
# #打印网页源代码


# from kkb_tools import open_file
import requests
# 引入requests
import csv

# 引用csv。
csv_file = open('articles.csv', 'w', newline='', encoding='utf-8')
# 调用open()函数打开csv文件，传入参数：文件名“articles.csv”、写入模式“w”、newline=''。
writer = csv.writer(csv_file)
# 用csv.writer()函数创建一个writer对象。

headers = {
    # ':authority':' www.zhihu.com',
    # ':method':' GET',
    # ':path':' /api/v4/members/lisanshui1230/articles?include=data%5B*%5D.comment_count%2Csuggest_edit%2Cis_normal%2Cthumbnail_extra_info%2Cthumbnail%2Ccan_comment%2Ccomment_permission%2Cadmin_closed_comment%2Ccontent%2Cvoteup_count%2Ccreated%2Cupdated%2Cupvoted_followees%2Cvoting%2Creview_info%2Cis_labeled%2Clabel_info%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=10&limit=10&sort_by=created',
    # ':scheme':' https',
    'accept': '*/*',
    # 'accept-encoding':'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': '_zap=06e20587-6f24-4b13-aa29-11044c6c017e; d_c0="ACAcDNcUXRGPTleC9E3O4eYjaXIpROQFXa4=|1591084363"; _ga=GA1.2.2130656072.1591084362; _xsrf=38cb55df-02ff-4871-abbf-a96910fc1d57; l_n_c=1; n_c=1; z_c0=Mi4xWUVkTkNnQUFBQUFBSUJ3TTF4UmRFUmNBQUFCaEFsVk45dm5xWHdCejFUTzlyM0dNWUplaWRSRmVfd3JWWlZHalhR|1593682934|302e491b7838c81bc2af27b8f617fc8a85f89e1d; q_c1=6969c96d746a4d37bac78a6828ba00fc|1595389702000|1595389702000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1595502463,1596102240,1596443516,1596449933; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1596623646; _gid=GA1.2.1429010679.1596623646; KLBRSID=57358d62405ef24305120316801fd92a|1596623733|1596623622',
    'referer': 'https://www.zhihu.com/people/lisanshui1230/posts?page=1',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'x-ab-param': 'li_svip_tab_search=1;li_panswer_topic=0;se_return_1=0;se_v_v005=0;tp_club_qa_entrance=1;ls_fmp4=0;se_v053=1;tp_club_top=0;li_yxxq_aut=A1;zw_sameq_sorce=999;zr_slotpaidexp=9;se_aa_base=0;li_catalog_card=1;li_viptab_name=0;qap_labeltype=1;se_preset=0;tp_club_fdv4=0;tp_club_entrance=1;li_pl_xj=0;qap_question_visitor= 0;zr_intervene=0;tp_topic_tab=0;pf_newguide_vertical=0;li_answer_card=0;zr_rec_answer_cp=open;zr_rerank=3;se_auth_src2=1;tp_zrec=1;li_topics_search=0;se_v058=0;soc_notification=1;zr_rel_search=base;zr_sim3=0;se_zp_boost=1;top_v_album=1;pf_creator_card=1;ug_follow_topic_1=2;ls_videoad=2;tp_club__entrance2=1;tp_sft=a;li_vip_verti_search=0;li_sp_mqbk=0;se_colorfultab=1;tp_topic_tab_new=0-0-0;li_video_section=1;zr_training_first=false;tp_club_feed=0;tp_club_bt=0;tp_topic_style=0;top_quality=0;pf_noti_entry_num=2;ls_recommend_test=4;se_mobilecard=0;se_merge=0;tp_dingyue_video=0;tp_contents=1;ls_video_commercial=0;se_usercard=0;se_recommend=0;se_vbert3=0;top_ebook=0;top_test_4_liguangyi=1;se_club_ui=0;se_major=0;se_wil_act=0;se_t2sug=1;se_searchwiki=0;top_universalebook=1;tsp_adcard2=0;ug_newtag=1;tsp_ioscard2=0;pf_adjust=1;zr_km_answer=open_cvr;zr_test_aa1=1;se_whitelist=1;se_v_v006=0;li_yxzl_new_style_a=1;tp_discover=1;tsp_hotlist_ui=3;se_col_boost=1;se_adsrank=4;se_ffzx_jushen1=0;zr_search_paid=1;se_hi_trunc=0;se_major_v2=0;tp_header_style=1;tsp_ios_cardredesign=0;li_ebook_gen_search=2;pf_foltopic_usernum=50;se_guess=0;li_edu_page=old;zr_ans_rec=gbrank;zr_training_boost=false;zr_search_sim2=2;se_topicfeed=0;qap_question_author=0;se_click_v_v=1;zr_art_rec=base;pf_profile2_tab=0;li_car_meta=1;se_sug_dnn=1;se_auth_src=0;soc_feed_intelligent=3;top_root=0;se_entity22=1;tp_m_intro_re_topic=1;tp_clubhyb=0;tp_flow_ctr=0;li_svip_cardshow=1;zr_expslotpaid=1;se_college=default;tp_fenqu_wei=0;se_videobox=0;zr_slot_training=2;zr_topic_rpc=0;se_v054=0;pf_fuceng=1;se_v057=0;se_sug_term=0;tsp_ad_cardredesign=0;li_paid_answer_exp=0;tp_meta_card=0',
    'x-ab-pb': 'CgqdCpsKJwolCpwKEgUAAAYFAQ==',
    # 'x-requested-with':' fetch',
    'x-zse-83': '3_2.0',
    'x-zse-86': '1.0_aLYBQi9BkXtfQ_N8YMF8Fb90e8xYUqN0fTS8UDrqHqFp',
}
# 封装headers
url = 'https://www.zhihu.com/api/v4/members/lisanshui1230/articles?include=data%5B*%5D.comment_count%2Csuggest_edit%2Cis_normal%2Cthumbnail_extra_info%2Cthumbnail%2Ccan_comment%2Ccomment_permission%2Cadmin_closed_comment%2Ccontent%2Cvoteup_count%2Ccreated%2Cupdated%2Cupvoted_followees%2Cvoting%2Creview_info%2Cis_labeled%2Clabel_info%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=10&limit=10&sort_by=created'
# 封装参数
res = requests.get(url, headers=headers)
# 发送请求，并把响应内容赋值到变量res里面
print(res.status_code)
# 确认请求成功
articles = res.json()
# 用json()方法去解析response对象，并赋值到变量articles上面，此时的articles是一个
data = articles['data']
# 取出键为data的值。
for i in data:
    article_info = [i['title'], i['url'], i['excerpt']]
    # 把目标数据封装成一个列表
    print(article_info)
    # 看看每行写入的内容
    writer.writerow(article_info)
# 遍历列表，拿到的是列表里的每一个元素，这些元素都是字典，再通过键把值取出来
csv_file.close()
# 写入完成后，关闭文件就大功告成

# open_file('articles.csv')
