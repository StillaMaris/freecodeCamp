def merge_sort(array):
    
    # Se l'array ha solo un elemento o meno non fa nulla
    # poiché un array con zero o un solo elemento è già ordinato.
    # Qui si esce dalla funzione
    if len(array) <= 1:
        return
    
    # Cerco la metà e divido l'array in due 
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # Metto in ordine le due parti separatamente ricorsivamente
    merge_sort(left_part)
    merge_sort(right_part)

    # Si inizializzano tre indici per tracciare le posizioni attuali 
    # nelle due metà e nell'array principale durante la fase di combinazione. 
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Ora il programma per mettere in ordine!
    
    
    # Si confrontano gli elementi delle due metà e 
    # si copiano gli elementi minori nell'array principale. 
    # Si incrementano gli indici appropriati per continuare il confronto.
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # Se ci sono elementi rimasti nella parte sx/dx
    # vengono copiati nell'array principale.
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


# Se il file è usato come main e non come modulo fa questo
if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ' + str(numbers))
