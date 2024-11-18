from code1 import total

def test_total_liste_vide():
	liste=[]
	res_obtenu=total(liste)
	res_attendu=0
	assert res_obtenu=res_attendu

def test_total_liste_non_content_un_element_non_null():
	liste=[5]
	res_obtenu=total(liste)
	res_attendu=0
	assert res_obtenu!=res_attendu


def test_total_liste_un_element_null():
	liste=[0]
	res_obtenu=total(liste)
	res_attendu=0
	assert res_obtenu=res_attendu


def test_total_liste_un_element_positif():
	liste=[7]
	res_obtenu=total(liste)
	res_attendu=7
	assert res_obtenu=res_attendu


def test_total_un_element_negatif():
	liste=[]
	res_obtenu=total(liste)
	res_attendu=0
	assert res_obtenu=res_attendu

def test_total_5_element():
	liste=[7,9,10,0,-1]
	res_obtenu=total(liste)
	res_attendu=25
	assert res_obtenu=res_attendu

def test_total_elements_negatifs():
	liste=[-1,-2,-5,-7]
	res_obtenu=total(liste)
	res_attendu=-15
	assert res_obtenu=res_attendu


def test_total_raises_exception_on_non_list_arguments():
    with pytest.raises(TypeError):
         total(1)
