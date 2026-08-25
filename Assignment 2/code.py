import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
SQUARE_IMAGE = "cat_18 (1).png"
RECTANGULAR_IMAGE = "cat_18.png"
EVD_K = [10, 50, 100]
SVD_K = [10, 50, 100]
RECT_K = [10, 50, 100]
def load_image(filename):
    image = Image.open(filename).convert("L")
    A = np.array(image,dtype=np.float64)
    return A
def show_image(A, title):
    display_image = np.real(A)
    display_image = np.clip(display_image,0,255)
    plt.figure(figsize=(7, 6))
    plt.imshow(display_image,cmap="gray",vmin=0,vmax=255)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
    plt.close()
def frobenius_error(A, Ak):
    return np.linalg.norm(A - Ak,ord="fro")
def find_conjugate_groups(eigenvalues,tolerance=1e-7):
    groups = []
    used = set()
    for i in range(len(eigenvalues)):
        if i in used:
            continue
        lam = eigenvalues[i]
        if abs(lam.imag) < tolerance:
            groups.append([i])
            used.add(i)
            continue
        conjugate = np.conjugate(lam)
        found = False
        for j in range(i + 1,len(eigenvalues)):
            if j in used:
                continue
            if np.isclose(eigenvalues[j],conjugate,atol=tolerance,rtol=tolerance):
                groups.append([i, j])
                used.add(i)
                used.add(j)
                found = True
                break
        if not found:
            groups.append([i])
            used.add(i)
    return groups
def group_score(group,eigenvalues):
    if len(group) == 2:
        lambda1 = eigenvalues[group[0]]
        lambda2 = eigenvalues[group[1]]
        product = (lambda1 * lambda2)
        return product.real
    lam = eigenvalues[group[0]]
    return lam.real ** 2
def sort_evd_groups(groups,eigenvalues):
    information = []
    for group in groups:
        score = group_score(group,eigenvalues)
        information.append((group,score))
    information.sort(key=lambda x: x[1],reverse=True)
    return information
def select_evd_components(sorted_groups,K):
    selected_indices = []
    actual_k = 0
    for group, score in sorted_groups:
        group_size = len(group)
        if (actual_k + group_size <= K):
            selected_indices.extend(group)
            actual_k += group_size
        else:
            break
    return (selected_indices,actual_k)
def reconstruct_evd(eigenvalues,Q,Q_inverse,selected_indices):
    n = len(eigenvalues)
    Lambda_k = np.zeros((n, n),dtype=np.complex128)
    for i in selected_indices:
        Lambda_k[i, i] = (eigenvalues[i])
    Ak = (Q @ Lambda_k @ Q_inverse)
    return Ak

def reconstruct_svd(U,S,Vt,K):
    Uk = U[:, :K]
    Sigma_k = np.diag(S[:K])
    Vtk = Vt[:K, :]
    Ak = (Uk @ Sigma_k @ Vtk)
    return Ak
def show_evd_reconstructions(original,reconstructions,k_values,actual_k_values):
    for i, Ak in enumerate(reconstructions):
        K = k_values[i]
        actual_K = actual_k_values[i]
        reconstructed_image = np.real(Ak)
        reconstructed_image = np.clip(reconstructed_image,0,255)
        error_image = np.abs(original - Ak)
        plt.figure(figsize=(15, 5))
        plt.subplot(1, 3, 1)
        plt.imshow(original,cmap="gray",vmin=0,vmax=255)
        plt.title(f"Original Image\nK = {K}")
        plt.axis("off")
        plt.subplot(1, 3, 2)
        plt.imshow(reconstructed_image,cmap="gray",vmin=0,vmax=255)
        plt.title(f"EVD Reconstruction\n"f"Requested K = {K}\n"f"Actual K = {actual_K}")
        plt.axis("off")
        plt.subplot(1, 3, 3)
        plt.imshow(error_image,cmap="gray")
        plt.title(f"Error Image |A - Ak|\n"f"K = {K}")
        plt.axis("off")
        plt.suptitle(f"EVD Image Reconstruction - K = {K}",fontsize=16)
        plt.tight_layout(rect=[0, 0, 1, 0.93])
        plt.show()
        plt.close()
        error = np.linalg.norm(original - Ak,ord="fro")
        print("\n")
        print(f"EVD RESULTS FOR K = {K}")
        print(f"Requested K: {K}")
        print(f"Actual K: {actual_K}")
        print(f"Frobenius Error ||A-Ak||F: {error:.6f}")
        print(f"Maximum imaginary value : "f"{np.max(np.abs(Ak.imag)):.10e}")
def show_svd_reconstructions(original,reconstructions,k_values,title):
    for i, Ak in enumerate(reconstructions):
        K = k_values[i]
        reconstructed_image = np.clip(Ak,0,255)
        error_image = np.abs(original - Ak)
        plt.figure(
            figsize=(15, 5)
        )
        plt.subplot(1, 3, 1)
        plt.imshow(original,cmap="gray",vmin=0,vmax=255)
        plt.title(f"Original Image\nK = {K}")
        plt.axis("off")
        plt.subplot(1, 3, 2)
        plt.imshow(
            reconstructed_image,
            cmap="gray",
            vmin=0,
            vmax=255
        )
        plt.title(            f"SVD Reconstruction\nK = {K}")
        plt.axis("off")
        plt.subplot(1, 3, 3)
        plt.imshow(
            error_image,
            cmap="gray",
            vmin=0,
            vmax=np.max(error_image)
        )
        plt.title(
            f"Error Image |A - Ak|\n"
            f"K = {K}"
        )
        plt.axis("off")
        plt.suptitle(
            f"{title} - K = {K}",
            fontsize=16
        )
        plt.tight_layout(
            rect=[0, 0, 1, 0.93]
        )
        plt.show()
        plt.close()
        error = np.linalg.norm(
            original - Ak,
            ord="fro"
        )
        print("\n")
        print(f"SVD RESULTS FOR K = {K}")
        print(  f"K  : {K}")
        print(f"Frobenius Error ||A-Ak||F: {error:.6f}")
def plot_error_graph(
    k_values,
    errors,
    title):
    plt.figure(figsize=(9, 6))
    plt.plot(
        k_values,
        errors,
        marker="o",
        markersize=4,
        linewidth=1.5
    )
    plt.xlabel("Number of Retained Components (K)")
    plt.ylabel("Frobenius Reconstruction Error")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()
print("\n")
print("SQUARE IMAGE - EVD")
A = load_image(SQUARE_IMAGE)
print("Square image shape:",A.shape)
if A.shape[0] != A.shape[1]:
    raise ValueError("EVD requires a square image matrix.")
show_image(
    A,
    "Square Image - Original"
)
print("\nPerforming EVD...")
eigenvalues, Q = np.linalg.eig(A)
Q_inverse = np.linalg.inv(Q)
print("EVD completed.")
print("Total eigenvalues:",len(eigenvalues))
A_full = (Q @ np.diag(eigenvalues) @ Q_inverse)
full_evd_error = frobenius_error(
    A,
    A_full
)
print("\n")
print("FULL EVD VERIFICATION")
print("Full EVD Frobenius Error:",full_evd_error)
print("Maximum imaginary value in full EVD:",np.max(np.abs(A_full.imag)))
groups = find_conjugate_groups(eigenvalues)
real_count = 0
complex_pair_count = 0
for group in groups:
    if len(group) == 1:
        real_count += 1
    elif len(group) == 2:
        complex_pair_count += 1
print("\n")
print("EIGENVALUE INFORMATION")
print("Total eigenvalues:",len(eigenvalues))
print("Real eigenvalues:",real_count)
print("Complex conjugate pairs:",complex_pair_count)
sorted_groups = sort_evd_groups(groups,eigenvalues)
print("\n")
print("COMPLEX CONJUGATE PAIRS")
pair_number = 1
for group, score in sorted_groups:
    if len(group) == 2:
        lambda1 = eigenvalues[group[0]]
        lambda2 = eigenvalues[group[1]]
        product = (lambda1 * lambda2)
        print(f"\nPair {pair_number}")
        print("λ1 =",lambda1)
        print("λ2 =",lambda2)
        print("λ1 × λ2 =",product)
        print("Pair score =",score)
        pair_number += 1
evd_reconstructions = []
evd_errors = []
evd_actual_k = []
print("\n")
print("EVD RECONSTRUCTION")
for K in EVD_K:
    selected_indices, actual_k = (
        select_evd_components(
            sorted_groups,
            K))
    Ak = reconstruct_evd(
        eigenvalues,
        Q,
        Q_inverse,
        selected_indices    )
    error = frobenius_error(A,Ak)
    evd_reconstructions.append(Ak)
    evd_errors.append(error)
    evd_actual_k.append(actual_k)
    print("\n")
    print("Actual K:",actual_k)
    print("Frobenius Error ||A - Ak||F:",error)
    print("Maximum imaginary value in Ak:",np.max(np.abs(Ak.imag)))
show_evd_reconstructions(A,evd_reconstructions,EVD_K,evd_actual_k)
plot_error_graph(
    evd_actual_k,
    evd_errors,
    "EVD Reconstruction Error vs K"
)
print("\n")
print("SQUARE IMAGE - SVD")
U, S, Vt = np.linalg.svd(A,full_matrices=False)
print("Number of singular values:",len(S))
print("\n")
print("FIRST 10 SINGULAR VALUES - SQUARE IMAGE")
for i in range(min(10, len(S))):
    print(f"σ{i + 1} = {S[i]:.6f}")
svd_reconstructions = []
svd_errors = []
svd_display_k = []
print("\n")
print("SVD RECONSTRUCTION - SQUARE IMAGE")
for K in SVD_K:
    if K > len(S):
        print(f"K = {K} skipped.")
        continue
    Ak = reconstruct_svd(U,S,Vt,K)
    error = frobenius_error(A,Ak)
    svd_reconstructions.append(Ak)
    svd_errors.append(error)
    svd_display_k.append(K)
    print("\n")
    print("K:",K)
    print("Frobenius Error ||A - Ak||F:",error)
show_svd_reconstructions(
    A,
    svd_reconstructions,
    svd_display_k,
    "SVD Reconstruction and Error - Square Image"
)
svd_all_k = []
svd_all_errors = []
for K in range(1,len(S) + 1):
    Ak = reconstruct_svd(U,S,Vt,K)
    error = frobenius_error(A,Ak)
    svd_all_k.append(K)
    svd_all_errors.append(error)
plot_error_graph(svd_all_k,svd_all_errors,"SVD Reconstruction Error vs K - Square Image")
print("\n")
print("EVD VS SVD COMPARISON")
print(f"{'EVD Actual K':<18}"f"{'EVD Error':<20}"f"{'SVD Error':<20}")
for i in range(len(EVD_K)):
    print(f"{EVD_K[i]:<15}"f"{evd_actual_k[i]:<18}"f"{evd_errors[i]:<20.6f}"f"{svd_errors[i]:<20.6f}")
plt.figure(figsize=(9, 6))
plt.plot(evd_actual_k,evd_errors,marker="o",label="EVD")
plt.plot(svd_display_k,svd_errors,marker="s",label="SVD")
plt.xlabel("Number of Retained Components (K)")
plt.ylabel("Frobenius Reconstruction Error")
plt.title("EVD vs SVD Reconstruction Error")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
plt.close()
print("\n")
print("RECTANGULAR IMAGE - SVD")
A_rect = load_image(RECTANGULAR_IMAGE)
print("Rectangular image shape:",A_rect.shape)
U_rect, S_rect, Vt_rect = np.linalg.svd(A_rect,full_matrices=False)
max_rank = len(S_rect)
print("Maximum rank:",max_rank)
print("\n")
print("FIRST 10 SINGULAR VALUES - RECTANGULAR IMAGE")
for i in range(min(10, len(S_rect))):
    print(f"σ{i + 1} = {S_rect[i]:.6f}")
rect_reconstructions = []
rect_errors = []
rect_display_k = []
print("\n")
print("SVD RECONSTRUCTION - RECTANGULAR IMAGE")
for K in RECT_K:
    if K > max_rank:
        print(f"K = {K} skipped because "f"maximum rank is {max_rank}.")
        continue
    Ak = reconstruct_svd(U_rect,S_rect,Vt_rect,K)
    error = frobenius_error(A_rect,Ak)
    rect_reconstructions.append(Ak)
    rect_errors.append(error)
    rect_display_k.append(K)
    print("\n")
    print("K:",K)
    print("Frobenius Error ||A - Ak||F:",error)
show_svd_reconstructions(A_rect,rect_reconstructions,rect_display_k,"SVD Reconstruction and Error - Rectangular Image")
rect_all_k = []
rect_all_errors = []
for K in range(1,max_rank + 1):
    Ak = reconstruct_svd(U_rect,S_rect,Vt_rect,K)
    error = frobenius_error(A_rect,Ak)
    rect_all_k.append(K)
    rect_all_errors.append(error)
plot_error_graph(rect_all_k,rect_all_errors,"SVD Reconstruction Error vs K - Rectangular Image")
