from owlready2 import *
from rdflib import *
from .teacher import Teacher
from .product import Product
from .subject import Subject

def get_value(value):
    if len(value) > 0:
        return value[0]

def build_subject(data, fetch=False):
    bm = Subject()
    bm.id = data._name
    bm.name = get_value(data.TEN_BM)

    if fetch:
        teachers = []
        for item in data.bm_co_gv:
            gv = build_teacher(item)
            teachers.append(gv)
        bm.teachers = teachers

        products = []
        for item in data.bm_co_sp:
            sp = build_product(item)
            products.append(sp)
        bm.products = products
    return bm

def build_teacher(data, fetch=False):
    gv = Teacher()
    gv.id = data._name
    gv.name = get_value(data.HO_TEN)
    gv.birthdate = get_value(data.NGAY_SINH).strftime('%d/%m/%Y')
    gv.birthplace = get_value(data.NOI_SINH)
    gv.hometown = get_value(data.QUE_QUAN)
    gv.address = get_value(data.DIA_CHI)
    gv.year = get_value(data.NamVaoNganh)
    gv.email = get_value(data.EMAIL)
    gv.phone = get_value(data.SDT)

    if fetch:
        gv.subject = build_subject(data.thuoc_bo_mon[0])
        cv = get_value(data.GV_co_CV)
        if cv:
            gv.title = get_value(cv.TEN_CV)

        products = []
        for item in data.la_tac_gia_cua:
            sp = build_product(item)
            products.append(sp)
        gv.products = products
    return gv

def build_product(data, fetch=False):
    sp = Product()
    sp.id = data._name
    sp.name = get_value(data.TEN_SP)
    sp.link = get_value(data.link)
    sp.summary = get_value(data.tom_tat)
    
    if fetch:
        sp.subject = build_subject(data.sp_thuoc_bm[0])
        sp.year = get_value(get_value(data.thuoc_ve_nam_hoc).TEN_CV)

        teachers = []
        for item in data.duoc_viet_boi:
            gv = build_teacher(item)
            teachers.append(gv)
        sp.teachers = teachers
    return sp

class Ontology:
    def __init__(self, filename):
        self.world = World()
        self.onto = self.world.get_ontology(filename).load()
        self.graph = self.world.as_rdflib_graph()
    
    def search_teachers(self, query):
        queryString = 'PREFIX dt:<http://www.semanticweb.org/quanlidetai#> SELECT ?tengv WHERE { ?tengv dt:HO_TEN ?ten FILTER regex(?ten, "%s")}' % query
        result = list(self.graph.query(queryString))

        teachers = []
        for item in result:
            gv = build_teacher(self.world[str(item['tengv'])])
            teachers.append(gv)
        return teachers

    def get_teachers(self):
        teachers = []
        for item in self.onto.GIAO_VIEN.instances():
            gv = build_teacher(item)
            teachers.append(gv)
        return teachers

    def get_teacher(self, id):
        item = self.onto.GIAO_VIEN(id)
        return build_teacher(item, fetch=True)

    def search_products(self, query):
        queryString = 'PREFIX dt:<http://www.semanticweb.org/quanlidetai#> SELECT ?tensp WHERE { ?tensp dt:TEN_SP ?ten FILTER regex(?ten, "%s")}' % query
        result = list(self.graph.query(queryString))

        products = []
        for item in result:
            sp = build_product(self.world[str(item['tensp'])], fetch=True)
            products.append(sp)
        return products

    def get_products(self):
        products = []
        for item in self.onto.SANPHAM.instances():
            sp = build_product(item, fetch=True)
            products.append(sp)
        return products

    def get_product(self, id):
        item = self.onto.SANPHAM(id)
        return build_product(item, fetch=True)

    def get_subjects(self):
        subjects = []
        for item in self.onto.TO_BO_MON.instances():
            bm = build_subject(item)
            subjects.append(bm)
        return subjects
    
    def get_subject(self, id):
        item = self.onto.TO_BO_MON(id)
        return build_subject(item, fetch=True)
